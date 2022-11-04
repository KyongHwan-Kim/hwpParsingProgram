NI Registry::HKEY_CURRENT_USER\SOFTWARE\HNC\HwpAutomation\Modules
New-ItemProperty Registry::HKEY_CURRENT_USER\SOFTWARE\HNC\HwpAutomation\Modules -Name AutomationModule -Value $pwd\FilePathCheckerModuleExample.dll
