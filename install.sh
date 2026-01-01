#!/bin/bash

# Renkler
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================================${NC}"
echo -e "${GREEN}   Gazi Siber Fetch Kurulum Aracı v1.0   ${NC}"
echo -e "${BLUE}================================================${NC}"

# 1. Fastfetch Yüklü mü Kontrol Et
if ! command -v fastfetch &> /dev/null; then
    echo -e "${RED}[!] Fastfetch bulunamadı.${NC}"
    echo "Lütfen önce sisteminize fastfetch yükleyin."
    echo "Ubuntu/Debian için: sudo add-apt-repository ppa:zhangsongcui3336/fastfetch -y && sudo apt update && sudo apt install fastfetch -y"
    exit 1
fi

# 2. Config Klasörünü Oluştur
CONFIG_DIR="$HOME/.config/fastfetch"
mkdir -p "$CONFIG_DIR"

echo "⚙️  Yapılandırma dosyaları indiriliyor..."

# 3. Dosyaları GitHub'dan Çek (Kendi kullanıcı adını buraya yazmayı unutma!)
REPO_URL="https://raw.githubusercontent.com/AbdullahZeynel/gazisiber-fetch/main"

# Config dosyasını indir
curl -sL "$REPO_URL/config.jsonc" -o "$CONFIG_DIR/gazisiber_config.jsonc"

# Logo dosyasını indir
curl -sL "$REPO_URL/logo_ascii.txt" -o "$CONFIG_DIR/logo_ascii.txt"

# 4. Config Dosyasındaki Logo Yolunu Düzelt
# İndirilen config dosyasındaki "~" işaretini kullanıcının tam ev dizini yoluyla değiştiriyoruz.
# Bu adım, dosya yolunun kesinlikle doğru çalışmasını sağlar.
sed -i "s|~/.config/fastfetch/logo_ascii.txt|$HOME/.config/fastfetch/logo_ascii.txt|g" "$CONFIG_DIR/gazisiber_config.jsonc"

echo "✅ Dosyalar $CONFIG_DIR konumuna yerleştirildi."

# 5. Global Komut Oluştur (gazisiber-fetch)
echo "🚀 'gazisiber-fetch' komutu oluşturuluyor (Sudo şifresi gerekebilir)..."

# /usr/local/bin içine bir script yazıyoruz
sudo bash -c "cat > /usr/local/bin/gazisiber-fetch" <<EOF
#!/bin/bash
fastfetch --config $HOME/.config/fastfetch/gazisiber_config.jsonc
EOF

# Çalıştırma izni ver
sudo chmod +x /usr/local/bin/gazisiber-fetch

echo -e "${GREEN}[✔] Kurulum Başarıyla Tamamlandı!${NC}"
echo -e "Terminale ${BLUE}gazisiber-fetch${NC} yazarak hemen deneyebilirsin."
