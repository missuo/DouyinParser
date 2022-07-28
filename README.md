# DouyinParser
A Powerful Douyin Video Parser

## Features
- [x] Parse no-watermark videos
- [x] Parse background music
- [x] Parse video titles
- [x] Parse author nickname
- [x] Parse author ID
- [x] No need to remove extra characters

## Usage
1. Install dependencies.
```bash
pip install DouyinParser
```
2. Create a new file with following codes.
```python
from DouyinParser import DouyinParser
DouyinParser.parser("https://v.douyin.com/FNUugSt/")
```
3. Get the result.
```json
{
   "desc":"请尽量快乐",
   "mp4":"https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200fg10000c9f375jc77u5ilfbm6rg&ratio=720p&line=0",
   "mp3":"https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/7088160680559250189.mp3",
   "nickname":"Mushini",
   "id":"None"
}
```

## Project on PyPI
- [missuo/DouyinParser](https://pypi.org/project/DouyinParser/)

## License
MIT License


