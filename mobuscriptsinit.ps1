Add-Type -AssemblyName PresentationCore,PresentationFramework
$msgBody = "Would you like to install this tool?"
$msgTitle = "Confirm Install"
$msgButton = 'YesNoCancel'
$msgImage = 'Question'
$Result = [System.Windows.MessageBox]::Show($msgBody,$msgTitle,$msgButton,$msgImage)

switch($Result){

'Yes'
{
python UserSetup.py
}
}