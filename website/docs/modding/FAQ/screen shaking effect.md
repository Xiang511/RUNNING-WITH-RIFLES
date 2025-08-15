---
description: How to Reduce/remove the screen shaking effect
tags:
  - Modding
  - Map
---

# How to Reduce/remove the screen shaking effect

Works in multiplayer Invasion! 

1. Right-click Running with Rifles in your Steam Library list and select Manage > Browse local files. This will open the directory where Steam installed the game on your machine.

2. Navigate from this folder down into the media/packages/vanilla/weapons directory.

3. Open artillery_shell.projectile with Notepad or another text editor.

4. In the result XML tag, replace push="1.5" with push="0".

5. Save the adjusted file and load into a new map in RWR to see the changes take effect.

:::tip
Repeat steps 3-5, as desired, for other projectiles (with a "blast" class for result) such as c4.projectile - the higher the push value (e.g. 3.0 for c4) the greater the shaking effect when the projectile blast happens; to reduce the shaking rather than removing it entirely, choose a smaller value for push such as 0.25.
:::










:::info

Author: warbong

https://discord.com/channels/181119538664964097/1376608143194325133

:::