#!/usr/bin/env node
const { execSync } = require("child_process");
const args = process.argv.slice(2).join(" ");
try {
  execSync(`skskyforge ${args}`, { encoding: "utf-8", stdio: "inherit" });
} catch (err) {
  process.exit(err.status || 1);
}
