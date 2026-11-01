# Location permission demo

This version requests geolocation as soon as the page loads. The page explains
that choosing Allow sends coordinates to the demo server; choosing Don't Allow
sends nothing. Browsers may suppress or defer permission prompts unless there
has been a user interaction. The site cannot override that browser decision.

Deploy by pushing the project files to GitHub and creating a Render Blueprint
from render.yaml. Render provides HTTPS, which is required for public geolocation.
