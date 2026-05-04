#!/usr/bin/env python3
from __future__ import annotations

"""
Fetch a YouTube transcript and save it as markdown under raw/transcripts/.

Usage:
    python tools/youtube2md.py "https://www.youtube.com/watch?v=..."
    python tools/youtube2md.py "https://youtu.be/..." --output raw/transcripts/custom.md
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "raw" / "transcripts"


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or f"youtube-{date.today().isoformat()}"


def get_video_id(url_or_id: str) -> str:
    patterns = [
        r"(?:v=)([A-Za-z0-9_-]{11})",
        r"(?:youtu\.be/)([A-Za-z0-9_-]{11})",
        r"(?:shorts/)([A-Za-z0-9_-]{11})",
        r"^([A-Za-z0-9_-]{11})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    raise ValueError("无法识别 YouTube video id")


def fetch_metadata(url: str) -> dict:
    try:
        import yt_dlp
    except ImportError:
        return {}

    opts = {"quiet": True, "skip_download": True, "noplaylist": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        return ydl.extract_info(url, download=False) or {}


def fetch_transcript(video_id: str, languages: list[str]) -> list[dict]:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError as exc:
        raise RuntimeError("缺少 youtube-transcript-api，请先运行 pip install -r requirements.txt") from exc

    try:
        if hasattr(YouTubeTranscriptApi, "get_transcript"):
            return YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        fetched = YouTubeTranscriptApi().fetch(video_id, languages=languages)
        return [
            {
                "text": snippet.text,
                "start": snippet.start,
                "duration": snippet.duration,
            }
            for snippet in fetched
        ]
    except Exception as exc:
        raise RuntimeError(f"无法获取转录：{exc}") from exc


def format_timestamp(seconds: float) -> str:
    seconds_int = int(seconds)
    h, rem = divmod(seconds_int, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def transcript_to_markdown(url: str, video_id: str, metadata: dict, rows: list[dict]) -> str:
    title = metadata.get("title") or f"YouTube {video_id}"
    channel = metadata.get("channel") or metadata.get("uploader") or ""
    upload_date = metadata.get("upload_date") or ""
    if len(upload_date) == 8:
        upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"

    body = "\n".join(
        f"- `{format_timestamp(float(row.get('start', 0)))}` {row.get('text', '').replace(chr(10), ' ').strip()}"
        for row in rows
        if row.get("text", "").strip()
    )

    return f"""---
title: "{title}"
type: source
tags: [youtube, transcript]
source_url: {url}
video_id: {video_id}
channel: "{channel}"
date: {upload_date or date.today().isoformat()}
---

# {title}

## 元数据

- 来源：{url}
- 频道：{channel or "未知"}
- 发布日期：{upload_date or "未知"}

## 转录

{body}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch a YouTube transcript and save it as markdown.")
    parser.add_argument("url", help="YouTube URL or 11-character video id")
    parser.add_argument("--output", help="Output markdown path")
    parser.add_argument("--languages", default="zh-Hans,zh-CN,zh,en", help="Comma-separated transcript language preferences")
    args = parser.parse_args()

    try:
        video_id = get_video_id(args.url)
        metadata = fetch_metadata(args.url)
        languages = [lang.strip() for lang in args.languages.split(",") if lang.strip()]
        rows = fetch_transcript(video_id, languages)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    title = metadata.get("title") or f"youtube-{video_id}"
    output = Path(args.output) if args.output else DEFAULT_OUTPUT_DIR / f"{slugify(title)}.md"
    if not output.is_absolute():
        output = REPO_ROOT / output

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(transcript_to_markdown(args.url, video_id, metadata, rows), encoding="utf-8")
    print(f"wrote: {output.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
