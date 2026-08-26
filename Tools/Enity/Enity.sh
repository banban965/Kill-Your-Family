#!/data/data/com.termux/files/usr/bin/bash

# ⚡ ENITY KILLER
# Termux + Shizuku/Rish

export RISH_APPLICATION_ID="com.termux"

RISH="$(command -v rish)"

clear

echo "╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮"
echo "┃     ⚡ ENITY KILLER        ┃"
echo "┃     🛑 FORCE STOP          ┃"
echo "╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯"
echo

# ───────── RISH ─────────

if [ -z "$RISH" ]; then
    echo "❌ rish پیدا نشد."
    exit 1
fi

echo "📍 Rish: $RISH"

# ───────── SHIZUKU TEST ─────────

SHIZUKU_ID="$("$RISH" -c 'id' 2>/dev/null)"

if [ -z "$SHIZUKU_ID" ]; then
    echo
    echo "❌ اتصال Shizuku برقرار نیست."
    echo
    echo "🔧 Test:"
    echo "RISH_APPLICATION_ID=com.termux rish -c 'id'"
    exit 1
fi

echo "✅ Shizuku: Connected"
echo "👤 $SHIZUKU_ID"
echo

# ───────── Protected ─────────

PROTECTED=(
    "com.termux"
    "moe.shizuku.privileged.api"
    "com.termux.api"
    "com.termux.widget"
    "com.termux.boot"
    "com.termux.tasker"
    "com.termux.styling"
    "com.termux.float"
)

is_protected() {
    local APP="$1"

    for P in "${PROTECTED[@]}"; do
        if [ "$APP" = "$P" ]; then
            return 0
        fi
    done

    return 1
}

# ───────── Apps ─────────

mapfile -t APPS < <(
    "$RISH" -c 'pm list packages -3' 2>/dev/null |
    sed 's/^package://' |
    while read -r APP; do
        if ! is_protected "$APP"; then
            echo "$APP"
        fi
    done
)

if [ "${#APPS[@]}" -eq 0 ]; then
    echo "❌ User App پیدا نشد."
    exit 1
fi

echo "📱 USER APPS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

for i in "${!APPS[@]}"; do
    printf "%3d) %s\n" "$((i+1))" "${APPS[$i]}"
done

echo
echo "00) 🌐 Select All"
echo "01) 🎯 Custom"
echo

read -rp "🎯 Select: " SELECT

SELECTED=()

if [ "$SELECT" = "00" ]; then

    SELECTED=("${APPS[@]}")

elif [ "$SELECT" = "01" ]; then

    read -rp "📌 Numbers (example: 1,2,4): " CUSTOM

    IFS=',' read -ra NUMS <<< "$CUSTOM"

    for N in "${NUMS[@]}"; do

        N="${N// /}"

        if [[ "$N" =~ ^[0-9]+$ ]] &&
           [ "$N" -ge 1 ] &&
           [ "$N" -le "${#APPS[@]}" ]; then

            SELECTED+=("${APPS[$((N-1))]}")

        fi

    done

else

    echo "❌ انتخاب نامعتبر."
    exit 1

fi

if [ "${#SELECTED[@]}" -eq 0 ]; then
    echo "❌ هیچ برنامه‌ای انتخاب نشده."
    exit 1
fi

# ───────── Thread ─────────

echo

read -rp "🧵 Thread [1-1000]: " THREAD

THREAD=${THREAD:-1}

if ! [[ "$THREAD" =~ ^[0-9]+$ ]] ||
   [ "$THREAD" -lt 1 ] ||
   [ "$THREAD" -gt 1000 ]; then
    THREAD=1
fi

# ───────── Think ─────────

echo

read -rp "🧠 Think Mode [y/n]: " THINK

RESET=0

if [[ "$THINK" =~ ^[Yy]$ ]]; then

    read -rp "⏱️ Reset Time [1-60 min]: " RESET
    RESET=${RESET:-1}

    if ! [[ "$RESET" =~ ^[0-9]+$ ]] ||
       [ "$RESET" -lt 1 ] ||
       [ "$RESET" -gt 60 ]; then
        RESET=1
    fi

fi

# ───────── Force Stop ─────────

force_stop() {

    local APP="$1"

    if is_protected "$APP"; then
        echo "🛡️ $APP → SKIPPED"
        return
    fi

    echo "🛑 $APP"

    if "$RISH" -c "am force-stop '$APP'" >/dev/null 2>&1; then
        echo "   └─ ✅ Force Stopped"
    else
        echo "   └─ ❌ Failed"
    fi
}

# ───────── Killer ─────────

run_killer() {

    echo
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "⚡ ENITY KILLER"
    echo "🛑 FORCE STOP"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    for APP in "${SELECTED[@]}"; do
        force_stop "$APP"
    done

    echo
    echo "✨ Cleanup Complete"
}

# ───────── Start ─────────

if [[ "$THINK" =~ ^[Yy]$ ]]; then

    echo
    echo "🧠 Think Mode: ON"
    echo "⏱️ Reset: ${RESET} min"
    echo "🛑 CTRL+C = Stop"
    echo

    while true; do

        run_killer

        echo
        echo "💤 Waiting ${RESET} minute(s)..."

        sleep "$((RESET * 60))"

        clear

    done