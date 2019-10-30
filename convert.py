import json
import pprint
import xlrd

convertedJsonData = {}
pp = pprint.PrettyPrinter(indent=4)

def main():
    with open("config.json") as configFile:
        config = json.load(configFile)
        loc = config["filename"]
        outputFile = config["outputFile"]

    wb = xlrd.open_workbook(loc)
    sheetNames = wb.sheet_names()

    with open(outputFile, "w+") as convertedJson:
        for sheetName in sheetNames:
            sheet = wb.sheet_by_name(sheetName)

            convertedJsonData[sheetName] = {}
            setHeaders(sheetName, sheet)
            setRows(sheetName, sheet)
        
        convertedJson.write(json.dumps(convertedJsonData))

def setHeaders(sheetName, sheet):
    convertedJsonData[sheetName]["headers"] = []
    for col in range(sheet.ncols):
        convertedJsonData[sheetName]["headers"].append(sheet.cell(0, col).value)

def setRows(sheetName, sheet):
    convertedJsonData[sheetName]["rows"] = []

    for row in range(1, sheet.nrows):
        newRow = {}
        for col in range(sheet.ncols):
            newRow[sheet.cell(0, col).value] = sheet.cell(row, col).value

        convertedJsonData[sheetName]["rows"].append(newRow)

if __name__ == "__main__":
    main()
    print ("DONE")
