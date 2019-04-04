# python-tv-parser **(PTP)**
PTP is an library for Playlist Parsing in Python

## Available FileTypes
- [ ] .M3U (in progress)
- [ ] .M3U8 (in progress)

## Parsing

Parsing a single file or a whole directory

### File
**ConvertFile function**:
returns an Dict Object with all TvElements in his group<br />
ex:
```
{
  "myGroup1": {
    "title": "MyCoolVideo"
  },
  "myGroup2": {
    "title": "MyCoolMusic"
  }
  ...
}
```

### Directory
**ConvertDirectory function**:
returns an Dict Object which contains other Dicts which represent the files,<br />
these Dicts contains the content of a singleFile <br />
ex:
```
{
  "MyFile1": {
    "myGroup1": [
      {
        "title": "MyCoolVideo"
      }
    ],
    "myGroup2": [
      {
        "title": "MyCoolMusic"
      }
    ]
    ...
  },
  "MyFile2": {
    "awesomeGroup1": [
      {
        "title": "MyCoolStream"
      }
    ],
    "awesomeGroup2": [
      {
        "title": "MyFunnyVideo"
      }
    ]
    ...
  }
}
```
