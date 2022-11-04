# hwpParsingProgram

병무청에서 매주 써야하는 유연근무제 HWP 파일 작성하기 귀찮아서 코드로 만들어보려고 함.

[주의]\
유연근무제 신청(변경)서.hwp 파일 수정 및 삭제 금지!\
FilePathCheckerModuleExample.dll 파일 이동 및 삭제 금지!

## Environment

- ### window 10
- ### 한글 프로그램

## Work Flow

### 1. 한글 보안 자동화를 위해 Window Registry 등록

registerSecurityModule.ps1 실행. or

```[powershell]
NI Registry::HKEY_CURRENT_USER\SOFTWARE\HNC\HwpAutomation\Modules
New-ItemProperty Registry::HKEY_CURRENT_USER\SOFTWARE\HNC\HwpAutomation\Modules -Name AutomationModule -Value $pwd\FilePathCheckerModuleExample.dll
```

### 2. defaultInfo.json 수정

한글 파일에 들어갈 기본 입력사항 입력 후 저장

```
{
  "companyName": "OOO 주식회사",
  "userTeam": "OO 본부",
  "userName": "홍길동",
  "birthday": "2XXX.XX.XX"
}
```

### 3. 실행

한글 파일에 들어갈 기본 입력사항 입력 후 저장
