import os
import win32com.client as win32


BASE_PATH = os.getcwd()
hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")

hwp.Open(BASE_PATH + "/유연근무제 신청(변경)서.hwp")
hwp.XHwpWindows.Item(0).Visible = True
print("\n", hwp.GetFieldList())

hwp.Run("SelectAll")  # Ctrl-A (전체선택)
hwp.Run("Copy")  # Ctrl-C (복사)
hwp.MovePos(3)  # 문서 끝으로 이동

# 8. 내용 붙여넣기
for i in range(3):
    hwp.Run("Paste")  # Ctrl-V (붙여넣기)
    hwp.MovePos(3)  # 문서 끝으로 이동
