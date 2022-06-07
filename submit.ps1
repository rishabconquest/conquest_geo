#!/usr/bin/env pwsh
# LF endings

$CURRENT_DATE=$(Get-Date)

$GIT_VERSION=$((git symbolic-ref HEAD).Split("/") | Select-Object -Last 1)

$VERSION="$GIT_VERSION.$($CURRENT_DATE.ToString("yyyyMMddHHmmss"))"

$COMMIT="$(git log --pretty=format:%h -1)"

cqservices submit `
--id            "49a4aabb-7855-497d-4453-7a1a6cd5f85d" `
--version       $VERSION `
--bundle        "zip_build/conquest_geo.zip" `
--commit        "$COMMIT" 
