# dash-inspector-downloader

This script allows to dowload locally the video segments logged by [dash-inspector](https://github.com/gdavila/dash-inspector) during a playback session.

## What it does

It parse the logfile obtained through [dash-inspector](https://github.com/gdavila/dash-inspector) in order to download the video segments locally for later analysis. All the representations are downloaded.

Additionally, once the video segments are downloaed, they are concatenated as a single video. One video is produced by each dash representation.

## How to use it

Just clone the repo and run `getDashSements.py`

```console
$ python3 getDashSements.py MediaFiles.json
```

`MediaFiles.json` is the file downloaded using [dash-inspector](https://github.com/gdavila/dash-inspector)