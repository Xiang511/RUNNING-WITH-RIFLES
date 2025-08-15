---
tags:
  - Modding
  - RWR voxel editor
---

More explanations on the Running With Rifles official forum topic : [RWR Voxel Editor 0.14](http://www.runningwithrifles.com/phpBB3/viewtopic.php?f=4&t=363)

## Launching



```
   rwr_editor.exe [model XML file] [animation XML file]
```
When launching the editor, an OGRE dialog pops up:
    - select the Rendering subsystem, there's only one choice.
    - I'd also recommend using the tool in non-fullscreen mode. Click OK to run the editor.
    - If the editor is launched without command line parameters, the editing happens on a model file "new.xml".
    - If such file doesn't exist, it will be created when the model is saved.


## Keys and other tips
   ### General
       - `WASD`: move around
       - `Left shift` + `ASDW`: move around faster
       - `Left shift` + `Mouse`: turn camera
       - `Ctrl-S`: save both model and animation files
       - `1`: Model view
       - `2`: Animation view, can be used only if the editor has been launched with a model with a skeleton
       - `O`: experimental magic tool that can be used to remove voxels that can't be seen from anywhere

    takes a long time to process, better save before doing this, not 100% foolproof, may also end up removing wrong voxels
    `ALT-F4`: quit-:)

   ### Model view
       - Edit voxels -tool:
           - `LMB`: add voxel
           - `RMB`: remove voxel
       - Select voxels -tool:
           - `LMB drag`:
                - define a rectangle selector for voxels
                - drag voxels around using the axis handles
       - To paint voxels, click on the current color indicator panel
       - When working with a model with a skeleton, and making modifications to the model,
        click "Re-bind skeleton" to attach the new voxels to the skeleton
   ### Animation view
       - `Left and right arrows`: previous / next keyframe
       - `Up and down arrows`: previous / next animation
       - Select & move -tool:
           - `LMB drag`:
               - define a rectangle selector for bone points which will be made movable
               - drag single bone point around and the other movable points will follow
       - To add a keyframe, click on the timeline, and displace a bone point
       - Currently, there's no playback button: simulate playback by dragging the timeline slider

:::note
This is a copy-pasted text from the first post by Pasik
:::
