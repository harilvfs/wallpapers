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

**SwayWM**
```bash
sudo pacman -S swaybg
