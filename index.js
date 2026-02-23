/**
 * @smilintux/skskyforge
 *
 * SKSkyforge - Sovereign Alignment Calendar System.
 * JS/TS bridge to the Python skskyforge package.
 * Install: pip install skskyforge
 */

const { execSync } = require("child_process");

const VERSION = "1.0.0";
const PYTHON_PACKAGE = "skskyforge";

function checkInstalled() {
  for (const py of ["python3", "python"]) {
    try {
      execSync(`${py} -c "import skskyforge"`, { stdio: "pipe" });
      return true;
    } catch {}
  }
  return false;
}

function run(args) {
  return execSync(`skskyforge ${args}`, { encoding: "utf-8" });
}

module.exports = { VERSION, PYTHON_PACKAGE, checkInstalled, run };
