### 🖼️ Wallpaper Collection 

Beautiful Nord & Anime Wallpapers Collection

### 📦 Sources:
- [🎨 2SSK's Wallpaper Bank](https://github.com/2SSK/Wallpaper-Bank)
- [❄️ ChrisTitusTech's Nord Background](https://github.com/christitustech/nord-background)

### 📋Usage:
Clone the repository:
 ```bash
 git clone https://github.com/harilvfs/wallpapers
 ```

### Wallpapers Packages [x11]
- feh
- nitrogen
- variety
- xfdesktop [xfce]
- hsetroot
- xwallpaper
- wallpaperd

```bash
sudo pacman -S feh nitrogen variety xfdesktop hsetroot xwallpaper wallpaperd
```

### Wallpapers Packages [Wayland]
- swaybg
- hyperbg
- feh (via XWayland)
- variety
- wally
- bgfx
- wpg
- hydrogen

```bash
sudo pacman -S swaybg variety
```
```bash
yay -S hyperbg feh wally bgfx wpg hydrogen
```

### Use Case with feh
```bash
sudo pacman -S feh
```
<strong> Use  the exec according to your window manager :
**Dwm**
```bash
  "sh", "-c", "feh --randomize --bg-fill ~/dir/wallpapers/*", NULL,
```

**i3wm**
```bash
exec --no-startup-id sh -c 'feh --randomize --bg-fill ~/dir/wallpapers/*'
```

**SwayWM** with  <strong>swaybg</strong>
```bash
sudo pacman -S swaybg
exec_always --no-startup-id swaybg -i ~/dir/wallpapers/ -m fill --randomize
```
