---
tags:
  - Modding
  - Create new Item
---

In campaign this is how to insert items into your singleplayer stash.

First in the RWR main menu you go to ***CONTINUE RECENT GAME***

Then you click ***MANAGE IN FILE BROWSER!***

Your campaign savegames should pop up.

Go to the campaign stash you want to edit.


in your campaign edit after the ```<stash>``` tag, you can place these tags in before the ```</stash>``` and it will appear in your campaign's stash.


## Item Number

| Item                        | Class Number |
|-----------------------------|--------------|
| Guns (.weapon)              | 0            |
| Grenades (.projectile)      | 1            |
| Vests/Misc Items (.carry_item) | 3        |
| Unknown                     | 2            |

:::info
All weapon names can be found in ```Steam_Root_Path\RunningWithRifles\media\packages\vanilla\weapons``` in ```all_weapons.xml``` as can ```all_throwables.xml```. Items like vests and misc items are found in ```Steam_Root_Path\RunningWithRifles\media\packages\vanilla\items``` in ```all_carry_items.xml```.

When adding items to stash, the "index" number doesn't seem to matter all too much, while testing i could set it to anything and the value would later become updated to correct number.
:::
:::note
If someone can clean up and better structure this new information, feel free. -Mews88

I realize only the rare weapons are listed. I'm working on finding the indexes and keys of the items. If anybody could help me with that message me or publish here. Thanks!

Also the stash limit has a limit of 100 items or 1000 weight. I'm not sure what happens if you go over the limit by placing objects in your stash, it might crash your save. If anybody tries adding items over the limit, let me know what happens.
:::



### RARE WEAPONS
```
<item class="0" index="124" key="javelin_ap.weapon" />
```
```
<item class="0" index="126" key="m16a4_support.weapon" />
```
```
<item class="0" index="8" key="m60e4.weapon" />
```
```
<item class="0" index="11" key="famasg1.weapon" />
```
```
<item class="0" index="13" key="f2000.weapon" />
```
```
<item class="0" index="14" key="benelli_m4.weapon" />
```
```
<item class="0" index="15" key="pepperdust.weapon" />
```
```
<item class="0" index="18" key="aks74u.weapon" />
```
```
<item class="0" index="19" key="p90.weapon" />
```
```
<item class="0" index="23" key="vss_vintorez.weapon" />
```
```
<item class="0" index="24" key="ns2000.weapon" />
```
```
<item class="0" index="29" key="stoner_lmg.weapon" />
```
```
<item class="0" index="30" key="m79.weapon" />
```
```
<item class="0" index="34" key="l85a2.weapon" />
```
```
<item class="0" index="35" key="sg552.weapon" />
```
```
<item class="0" index="41" key="mg_resource.weapon" />
```
```
<item class="0" index="51" key="xm25.weapon" />
```
```
<item class="0" index="52" key="desert_eagle.weapon" />
```
```
<item class="0" index="53" key="desert_eagle_gold.weapon" />
```
```
<item class="0" index="54" key="aa-12.weapon" />
```
```
<item class="0" index="55" key="mgl_flasher.weapon" />
```
```
<item class="0" index="56" key="barrett_m107.weapon" />
```
```
<item class="0" index="57" key="xm8.weapon" />
```
```
<item class="0" index="72" key="microgun.weapon" />
```
```
<item class="0" index="74" key="javelin.weapon" />
```
```
<item class="0" index="75" key="benelli_m4_supp.weapon" />
```
```
<item class="0" index="76" key="kriss_vector.weapon" />
```
```
<item class="0" index="77" key="javelin.weapon" />
```
```
<item class="0" index="81" key="mg42.weapon" />
```
```
<item class="0" index="82" key="lahti_l39.weapon" />
```
```
<item class="0" index="83" key="sawnoff.weapon" />
```
```
<item class="0" index="84" key="milkor_mgl.weapon" />
```
```
<item class="0" index="88" key="steyr_aug.weapon" />
```
```
<item class="0" index="90" key="scarssr.weapon" />
```
```
<item class="0" index="92" key="chain_saw.weapon" />
```
```
<item class="0" index="93" key="pecheneg_bullpup.weapon" />
```
```
<item class="0" index="100" key="honey_badger.weapon" />
```
```
<item class="0" index="103" key="jackhammer.weapon" />
```
```
<item class="0" index="104" key="uts15.weapon" />
```
```
<item class="0" index="105" key="smaw.weapon" />
```
```
<item class="0" index="107" key="ares_shrike.weapon" />
```
```
<item class="0" index="108" key="paw20.weapon" />
```
```
<item class="0" index="112" key="taser.weapon" />
```
```
<item class="0" index="114" key="flamethrower.weapon" />
```
```
<item class="0" index="115" key="aa12_frag.weapon" />
```
```
<item class="0" index="121" key="dartgun.weapon" />
```
```
<item class="0" index="122" key="fal_bayonet.weapon" />
```
```
<item class="0" index="123" key="golden_knife.weapon" />
```
```
<item class="0" index="125" key="l30p.weapon" />
```
```
<item class="0" index="127" key="tti.weapon" />
```

### Vests/Misc Items

```
<item class="3" index="70" key="camo_vest.carry_item" />
```
```
<item class="3" index="18" key="vest3.carry_item" />
```
```
<item class="3" index="23" key="bible.carry_item" />
```
```
<item class="3" index="44" key="suitcase.carry_item" />
```
```
<item class="3" index="58" key="costume_clown.carry_item" />
```
```
<item class="3" index="59" key="costume_santa.carry_item" />
```
```
<item class="3" index="60" key="vest_blackops.carry_item" />
```
```
<item class="3" index="67" key="costume_lizard.carry_item" />
```
```
<item class="3" index="66" key="gift_box_community_1.carry_item" />
```
```
<item class="3" index="75" key="gift_box_community_2.carry_item" />
```
```
<item class="3" index="69" key="costume_banana.carry_item" />
```

### Stationary

```
<item class="0" index="44" key="deployable_minig.weapon" />
```
    
### Throwables

```
<item class="1" index="55" key="dooms_hammer.projectile" />
```
```
<item class="1" index="52" key="aav7_flare.projectile" />
```
```
<item class="1" index="50" key="wiesel_flare.projectile" />
```
```
<item class="1" index="53" key="banana_peel.projectile" />
```
