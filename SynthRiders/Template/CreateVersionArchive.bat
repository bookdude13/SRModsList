set BUILT_VERSION=1.1.1
set MOD_NAME=SRPlaylistManager

set LOCAL_ITEM_FILE=.\LocalItem.json
echo {"hash": "%MOD_NAME%"} > %LOCAL_ITEM_FILE%

set ROOT_OUTPUT_DIR=..\Downloads
set MODS_DIR=.\Mods

set OUTPUT_DIR=%ROOT_OUTPUT_DIR%\%MOD_NAME%
mkdir %OUTPUT_DIR%

powershell Compress-Archive -Path %MODS_DIR%,%LOCAL_ITEM_FILE% -DestinationPath %OUTPUT_DIR%\%MOD_NAME%_%BUILT_VERSION%.zip
move %OUTPUT_DIR%\%MOD_NAME%_%BUILT_VERSION%.zip %OUTPUT_DIR%\%MOD_NAME%_%BUILT_VERSION%.synthmod
