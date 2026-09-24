# Start Your Workspace

## Lab Objective

**Start the AI Governance Workspace on your lab VM, and open it in your browser.**

Every lab in this course runs inside one web app. Before you can begin 1.1, that app needs to be running on your lab VM. This takes one command and about a minute.

## In Plain Words

- **What you are doing:** running one command that starts your workspace, then opening it in your browser.
- **Why it matters:** every lab, every answer box, and every reading in this course lives inside that workspace. Nothing else needs to be installed or downloaded.
- **You do not have to:** worry about losing your work. Everything you type in the workspace saves itself as you go, so even if your browser crashes, your tab closes, or you come back tomorrow, your answers will still be there.

## Step 1: Start the workspace

Open a terminal on your lab VM and run:

```bash
docker run -d --name governance --restart unless-stopped \
  -p 2224:2224 -v governance-data:/data \
  ghcr.io/csfeeser/ai-governance-workspace:latest
```

This downloads the workspace and starts it running in the background. You only need to run it once; it keeps running even if you close the terminal.

## Step 2: Open the workspace

Click the `WEB PORTS` dropdown in your classroom environment. From that menu, click `aux1:2224`. This opens the workspace in a new browser tab.

## If your page crashes or closes

Your progress is never sitting only in the browser. Every answer you type saves to the workspace itself the moment you type it, not to your browser tab. So if your page crashes, your tab closes, your VM reboots, or you simply come back the next day, nothing is lost: click `WEB PORTS` -> `aux1:2224` again, and your workspace, with every answer you have saved, will be exactly as you left it.

## Resources

- Once the workspace is open, click `1.1 Set the Business Quality Standard` in the left sidebar to begin the course.
