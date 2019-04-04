# python-tv-parser **(PTP)**
PTP is an lightweight Python library for parsing common Playlist File Types

## Available FileTypes
- [X] .M3U (ready for test)
- [X] .M3U8 (ready for test)

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
these Dicts contains the content of a singleFile <br />
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
