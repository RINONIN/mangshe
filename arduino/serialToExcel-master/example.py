from serialToExcel import SerialToExcel

serialToExcel = SerialToExcel("COM5", 9600)

serialToExcel.setColumns(["序号", "参数"])
serialToExcel.setRecordsNumber(500)
serialToExcel.readPort()

serialToExcel.writeFile("data2.xls")
