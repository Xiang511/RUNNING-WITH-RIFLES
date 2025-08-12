## Example
```
<vehicle file="vehicle_base.vehicle" name="quad" key="atv_base.vehicle" map_view_atlas_index="27" minimum_fill_requirement="1">
	<tag name="metal_thin" />
	<tag name="atv" />

	<tire_set offset="0.7 0.0 0.9" radius="0.45" />
	<tire_set offset="0.7 0.0 -0.9" radius="0.45" />

	<control max_speed="28.0" acceleration="9.7" max_reverse_speed="5.0" max_rotation="0.5" max_water_depth="1.4" steer_smoothening="0.7" />

	<physics max_health="0.5" mass="1.0" extent="1.6 0.0 3.0" offset="0 0.0 0.0" top_offset="0 0.6 0" collision_model_pos="0.0 0.6 0.0" collision_model_extent="1.8 1.65 3.4" visual_offset="0 0.15 0" gravity="-38" friction_offset="0.1"  drag_offset="-0.25" />  


	<visual class="chassis" mesh_filename="atv_body.mesh" texture_filename="atv.png" max_tilt="0.04" />
	<visual class="chassis" key="broken" mesh_filename="atv_body_broken.mesh" texture_filename="atv_broken.png" />
 	<visual class="front_tire" mesh_filename="atv_wheel_front.mesh" texture_filename="atv_wheel_front.png" />
	<visual class="rear_tire" mesh_filename="atv_wheel_back.mesh" texture_filename="atv_wheel_back.png" />

	<character_slot type="driver" position="0.0 0.55 -0.4" rotation="0" exit_rotation="1.57" hiding="0" animation_key="driving atv" />
	<character_slot type="passenger" position="0.0 0.75 -1.2" rotation="0" exit_rotation="3.14" hiding="0" animation_key="passenger atv" />


	<!-- sound handling -->
	<rev_sound filename="atv_rev0.wav" low_pitch="1.2" high_pitch="1.5" low_rev="0.0" high_rev="0.4" volume="0.6" />
	<rev_sound filename="atv_rev1.wav" low_pitch="0.6" high_pitch="1.0" low_rev="0.3" high_rev="0.7" volume="0.6" />
	<rev_sound filename="atv_rev2.wav" low_pitch="0.8" high_pitch="1.0" low_rev="0.6" high_rev="1.0" volume="0.8" />
	<sound key="slide" filename="slide_noise.wav" volume="0.5" />
	<sound key="squeal" filename="tire_squeal.wav" volume="0.5" />
	<sound key="ignition" filename="truck_ignition.wav" volume="0.5" />
	<sound key="horn" filename="horn_jeep.wav" />   
	<sound key="hit" filename="car_hit1.wav" volume="0.5" />
	<sound key="hit" filename="car_hit2.wav" volume="0.5" />
	<sound key="hit" filename="car_hit3.wav" volume="0.5" />
	<sound key="destroy" filename="vehicle_explosion_1.wav" />   
	<sound key="cleanup" filename="vehicle_explosion_1.wav" />   

	<effect event_key="slide" type="splat_map" surface_tag="road" size="1.0" atlas_index="5" layer="0" />
	<effect event_key="slide_hard" type="splat_map" surface_tag="road" size="0.5" atlas_index="2" layer="0" />
	<effect event_key="slide" type="splat_map" surface_tag="dirt" size="1.0" atlas_index="2" layer="1" />
	<effect event_key="slide" type="particle" key="terrain" surface_tag="dirt" ref="Burst" use_surface_color="1" />
  
        <effect event_key="destroyed" ref="SmallSmokeVehicle" offset="-0.0 1.0 0.2" />
        <effect event_key="destroyed" ref="SmallSmokeVehicle" offset="-0.3 1.1 -1.3" />  
        <effect event_key="destroyed" ref="SmallFireRepeat" offset="0.0 0.7 0.2" />
        <effect event_key="destroy" key="other" ref="woosh" post_processing="0" shadow="0" />   
        <effect event_key="cleanup" key="other" ref="woosh" post_processing="0" shadow="0" />     

	<event>
		<trigger class="receive_damage" />
		<result class="reward" xp="0.0020" />
	</event>
  
	<event>
		<trigger class="spot" />
		<result class="reward" rp="10.0" />
	</event>

	<event>
		<trigger class="destroy" />
		<result class="reward" rp="10.0" />
	</event>
  
	<event>
		<trigger class="destroy" />
  	        <result class="spawn" instance_class="visual_item" instance_key="burning_piece_armor1.visual_item" min_amount="1" max_amount="3" offset="0 2.5 0" position_spread="1.5 1.5" direction_spread="0.15 0.3" />
	</event>
	<event>
		<trigger class="destroy" />  	
                <result class="spawn" instance_class="visual_item" instance_key="burning_piece_armor2.visual_item" min_amount="0" max_amount="1" offset="0 2.5 0" position_spread="1.5 1.5" direction_spread="0.10 0.25" />
	</event>
        <event>
                <trigger class="cleanup" />		
                <result class="spawn" instance_class="visual_item" instance_key="burning_piece_cleanup.visual_item" min_amount="20" max_amount="30" offset="0 2.0 0" position_spread="1.5 1.5" direction_spread="0.1 0.1" /> 
        </event>    
 	<event>
		<trigger class="cleanup" />
                <result class="spawn" instance_class="projectile" instance_key="debri_stun" min_amount="1" max_amount="1" offset="0 3.0 0" position_spread="0.0 0.0" direction_spread="0.0 0.0" />
        </event>   
</vehicle>
tbc.
```

## Modelling part - how to create the mesh
1. go to https://www.blender.org/ and download the latest version (as of today 2.77a proved as working - future version will probably work as well).

2. Install Blender.

3. go to https://code.google.com/archive/p/blender2ogre/downloads and download the latest add-on to export Blender models to `*.mesh` files which is a binary polygonal format that can be read by RWR (as of today blender2ogre 0.6.0 - future version will probably work as well).

4. Use Blender's interface, under File>user-preferences, click addons, click "install-addon", and select `io_export_ogreDotScene.py`

5. now you can select the model you imported/created and click file>export>Ogre 3D and it will export the required `*.mesh` file and a `*.scene file`, a `*.material` file and a `*.mesh.xml` (all not required for RWR.)

6. this is optional: you can install a tool called "OGRE meshy" which is a `*.mesh` file visualization tool (you can then directly double-click a `*.mesh` file and it will render it)

:::tip
 if `5.` doesn't export a `*.mesh` file but only a `*.mesh.xml` file you will have to download a dependancy like in the note below (from the README.TXT in the Ogre exporter archive you downloaded in `3.` )

           In order to create binary Ogre meshes, you need OgreXMLConverter.
           Try to use the latest Ogre tools, at the moment that would be 1.7
           
           Windows
               1. Download the latest Ogre Command-line tools from
                  http://www.ogre3d.org/download/tools
               2. Install to the default location.
               3. See "Setting Tool Paths" section if .mesh files
                  are not exported to configure the tools.