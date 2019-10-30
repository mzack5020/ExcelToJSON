# ExcelToJSON
## Description
Python script to convert Excel documents to JSON.

## Requirements
* Python 3
* Edit config file with your Excel filename and the output filename if you care to vary from the default of "converted.json". Absolute paths would work best but relative paths could work...

## Output
```JSON
{
  "headers": [
    "col1Header",
    "col2Header",
    "col3Header"
  ],
  "rows": [
    {
      "col1Header": "row1Col1Data",
      "col2Header": "row1Col2Data",
      "col3Header": "row1Col3Data"
    }, {
      "col1Header": "row2Col1Data",
      "col2Header": "row2Col2Data",
      "col3Header": "row2Col3Data"
    }, {
      "col1Header": "row3Col1Data",
      "col2Header": "row3Col2Data",
      "col3Header": "row3Col3Data"
    }
  ]
}
```
## Future Development Ideas
* Error checking needs to be fully integrated.
