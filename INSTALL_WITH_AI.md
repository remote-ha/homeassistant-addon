# Install Remote Home Assistant with an AI agent

Install **Remote Home Assistant** from the app store on the user's **Home Assistant OS** instance. Use the repository `https://github.com/remote-ha/homeassistant-addon`. Installation is complete once you verify the installed version and app status. Pairing is a separate step that requires an explicit request from the user. See the [Remote Home Assistant repository](https://github.com/remote-ha/homeassistant-addon#english).

## 1. Verify the target instance

1. Use the open Home Assistant UI. If it is closed, ask the user for the instance's local address. If multiple instances are available and the target is unclear, ask the user to identify the correct one. Let the user sign in and complete any MFA directly in the browser.
2. Open **Settings → System → Repairs → ⋮ → System information** and check the installation type and CPU architecture. The target instance must run **Home Assistant OS** on **`aarch64` (ARM64)** or **`amd64` (x86-64)**. Read the architecture from the target instance even if the agent runs on another device. See [Home Assistant system information](https://www.home-assistant.io/more-info/system-information/) and the [app manifest](./remote_home_assistant/config.yaml).
3. Check that the session has administrator privileges and can open the store under **Settings → Apps → Install app**. Before Home Assistant 2026.2, look for **Add-ons** and the add-on store. Stop and report the unmet requirement if the target runs Home Assistant Container or an unsupported architecture, if the session lacks privileges or store access, or if you cannot verify the requirements. See the [Home Assistant OS guide](https://www.home-assistant.io/common-tasks/os/#installing-a-third-party-app-repository) and the [app documentation](./remote_home_assistant/DOCS.md#english).

## 2. Install from the Home Assistant app store

1. Check the list of installed apps before adding the repository. If the app from the correct repository is already installed, report its version and status from the **Info** tab and skip reinstallation, updates, startup and configuration changes. If you find an earlier release from a different repository, report it and stop before making changes. Migration can interrupt an existing connection. See the [migration guidance](./remote_home_assistant/DOCS.md#english).
2. Open **Settings → Apps → Install app → ⋮ → Repositories**. If `https://github.com/remote-ha/homeassistant-addon` is missing from the list, paste it and select **Add**. Verify that the repository now appears in the list.
3. Close the repository dialog. Under **Remote Home Assistant Apps**, select **Remote Home Assistant**, then select **Install**. If the app is missing after you add the repository, refresh the store or select **Check for updates** if available. See the [repository installation instructions](./README.md#register-and-install).
4. Wait for the operation to finish. Return to the list of installed apps, open **Remote Home Assistant → Info**, and record the installed version and app status shown by the instance. If the user asked only for installation, stop here.

Use the Home Assistant app store for installation. Leave HACS, manual file copying, SSH, Docker and direct API calls out of the installation workflow. Preserve existing router settings, port forwarding, access rules and connections.

## 3. Pair and verify the tunnel if requested

1. Once the user explicitly asks to pair, open the Remote HA dashboard. Let the user sign in and select the installation or create one if needed. If pairing would replace an existing connection, stop and explain the conflict. Leave its token and device access in place. Open the [Remote HA dashboard](https://remote-ha.com/en/dashboard).
2. Identify the selected Remote HA installation and the local Home Assistant instance for the user. Explain that starting the tunnel enables remote access through the installation's address. **Get explicit confirmation before saving the token or starting the app.** A pairing request authorizes preparation. Wait for confirmation before enabling the tunnel. The app may be configured to start at boot. See the [app manifest](./remote_home_assistant/config.yaml) and the [Home Assistant app configuration reference](https://contributors.home-assistant.io/apps/reference/configuration/#information-and-behavior).
3. After confirmation, hand control of the browser to the user for the token step. The user selects **Pairing token** in the Remote HA dashboard, pastes the one-time token into **Settings → Apps → Remote Home Assistant → Configuration → Token**, then selects **Save**. Resume when the user confirms the save and closes any views that show the token. Keep tokens, passwords and MFA codes out of chat, tool history, screenshots and logs. Leave credential fields and the clipboard to the user. See the [Remote HA pairing instructions](./remote_home_assistant/DOCS.md#pair-your-home).
4. On the **Info** tab, select **Start**. If the app is already running and you have verified that it is unpaired, select **Restart** within the scope of the confirmed pairing. Leave any changes to **Start on boot** to the user.
5. Verify that the selected installation shows **Connected** in the Remote HA dashboard. Open its HTTPS address in a browser session with no active Home Assistant login and verify that you reach the **Home Assistant sign-in screen**. If a Remote HA access gate appears first, let the user authenticate there. End the test at the Home Assistant sign-in screen. Report the tunnel status and HTTPS test separately, including any check you could not complete. See the [app documentation](./remote_home_assistant/DOCS.md#pair-your-home).

## 4. Use MCP when available

MCP is optional. The tools exposed by the Home Assistant **Model Context Protocol** integration depend on the version, server configuration and session permissions. Verify app store, Supervisor and Remote HA dashboard access separately from MCP or entity control. See the [Home Assistant MCP server documentation](https://www.home-assistant.io/integrations/mcp_server/).

1. Verify which instance the MCP client is connected to. Inspect the tools listed by the client, or use the standard `tools/list` request if the client exposes it and the server declares tool support. Read every page and check the description, input schema and required permissions of each tool you plan to use. See the [MCP tools specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#listing-tools).
2. Use MCP to read the installation type, architecture, app status, installed version or relevant logs only when a tool in the current session explicitly supports that read for the target instance. Use the UI if a tool is missing, access is denied or the response is incomplete. Use documented tools and endpoints within the session's permissions.
3. Follow sections 1–3 in the browser to add the repository, install the app, have the user enter the token, start the app and test its address. Keep the pairing token in the app configuration form. If you only have MCP access, report that the UI is unavailable and tell the user where to take over. Leave the MCP server configuration, permissions and network exposure as they are.

## 5. Troubleshoot and report the outcome

| Stage | What to check |
| --- | --- |
| Repository or installation | Verify the repository URL, refresh the store and check the UI message. Under **Settings → System → Logs**, select **Supervisor**. After a timeout, check the installed apps list and the operation status before selecting **Install** again. |
| Token save or app startup | Check the validation message or the relevant part of the app's **Logs** tab. If the token has expired or was already used, the user can generate and enter a new one. Get confirmation before trying to start the app again. |
| Tunnel or HTTPS test | Check the app status, its logs and the selected installation's status in the dashboard. Report whether the tunnel itself failed to connect or the connected tunnel's HTTPS address returned an error or stopped at the access gate. |

See [Home Assistant OS logs](https://www.home-assistant.io/common-tasks/os/logs/) and the [Remote HA app documentation](./remote_home_assistant/DOCS.md#english).

Report the installation outcome as **installed**, **already installed**, **blocked** or **unverified**. Include the installed version and app status if available. Report pairing and the HTTPS test separately, marking either as skipped if applicable. For a failure, identify the stage, summarize the UI or log message and state what is needed to continue. Redact tokens, passwords, keys, authentication headers and URLs that contain secrets. If logs are unavailable or the message cannot be quoted safely, describe the observed symptom and what you were able to verify.
