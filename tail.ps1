Clear-Host

$FolderPath = "C:\Text-files\" # This is the path of the files to scan
$FileLast = gci -Path $FolderPath -File | Sort-Object -Property LastWriteTime -Descending | Select FullName -First 1 # Sorting to the latest updated file
$file = $FileLast.FullName # Get the full file name
Get-Content $file -Wait # Tail the file
