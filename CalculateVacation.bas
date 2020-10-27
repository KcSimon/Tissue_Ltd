Attribute VB_Name = "Module1"
Option Explicit

Function CalculateVacation(ByVal StrDate, ByVal CntType) As Double
    
    Dim vacRate As Double
    Dim dateDif As Integer

    dateDif = DateDifference(StrDate)

    If (dateDif >= 15) Then
        vacRate = ActiveWorkbook.Worksheets("Vacation Rate").Cells(13, 1).Value
    ElseIf (dateDif >= 12) Then
        vacRate = ActiveWorkbook.Worksheets("Vacation Rate").Cells(12, 1).Value
    ElseIf (dateDif >= 10) Then
        vacRate = ActiveWorkbook.Worksheets("Vacation Rate").Cells(11, 1).Value
    ElseIf (dateDif >= 5 Or CntType >= 8) Then
        vacRate = ActiveWorkbook.Worksheets("Vacation Rate").Cells(10, 1).Value
    ElseIf (dateDif >= 3 Or CntType >= 7) Then
        vacRate = ActiveWorkbook.Worksheets("Vacation Rate").Cells(9, 1).Value
    ElseIf (dateDif < 3 And CntType = 6) Then
        vacRate = ActiveWorkbook.Worksheets("Vacation Rate").Cells(8, 1).Value
    ElseIf (dateDif < 3 And CntType < 6 And CntType > 2) Then
        vacRate = ActiveWorkbook.Worksheets("Vacation Rate").Cells(7, 1).Value
    Else
        vacRate = 0
    End If

    CalculateVacation = vacRate * MonthsPassed(CDate("01-Oct-" & (Year(Now()) - 1)))
    
End Function

Function MonthsPassed(ByVal beginDate) As Integer
   
    If (DateDifference(beginDate) > 0) Then
        MonthsPassed = dateDiff("m", beginDate, Now())
    Else
        MonthsPassed = 0
    End If

End Function

Function DateDifference(ByVal pastDate) As Integer
    
    DateDifference = dateDiff("yyyy", pastDate, Now())
    
End Function
