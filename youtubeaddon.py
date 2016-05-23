import xbmc
import xbmcgui
import xbmcaddon

addon = xbmcaddon.Addon('plugin.video.vevotv')
title = addon.getAddonInfo('name')
link ='plugin://plugin.video.youtube/play/?video_id='

l1 = xbmcgui.ListItem(legal=title, iconImage=icon, thumnailImage=icon, path=link)
l1.setInfo(type="Video", infoLabels=("title": title))
l1.setProperty("IsPlayable", "true")

xbmc.Player().play(itemlink, listitem=li)
