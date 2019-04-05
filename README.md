# python-tv-parser **(PTP)**
PTP is an lightweight Python library for parsing common Playlist File Types

## Lightweight Parsing
The goal of this project is to make it lightweight as possible and take the best performance out of it. <br />
That's why we only want to parse the following information from the files: <br />
- title/name
- icon/logo
- url/source
- group (if possible)

## Requirements
tested on Python 2.7. <br />
All Python versions above 2.7 should work.<br />
Versions under 2.7 are untested

## Supported FileTypes
- [X] .M3U (ready for test)
- [X] .M3U8 (ready for test)

## Additional Features
- [ ] EPG Parsing (soon)

## Parsing
Parsing a single file or a whole directory

### File
**ConvertFile function**:
returns an Dict Object with all TvElements in his group<br />
example output:
```
{
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
}
```

### Directory
**ConvertDirectory function**:
returns an Dict Object which contains other Dicts which represent the files,<br />
these Dicts contains the content of a singleFile<br />
example output:
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
