$ErrorActionPreference = 'Stop'
$studioRoot = $PSScriptRoot
$studioNode = Get-Command node -ErrorAction SilentlyContinue
if ($studioNode) { $studioNodePath = $studioNode.Source } else { $studioNodePath = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' }
if (-not (Test-Path -LiteralPath $studioNodePath)) { throw 'Node.js not found. Open index.html directly instead.' }
Write-Host 'Open http://127.0.0.1:4186 in your browser. Press Ctrl+C to stop.'
& $studioNodePath (Join-Path $studioRoot 'tools/serve.mjs')
