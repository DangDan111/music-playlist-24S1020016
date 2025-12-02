songs = [
    {'Title': 'Hồng nhan', 'artist': 'Jack', 'duration': '2019'},
    {'Title': 'Bạc Phận', 'artist': 'Jack', 'duration': '2019'}
]
def add_song(title: str, artist: str, duration: int) -> dict:
    """
    Thêm bài hát vào songs, trả về dict bài hát.
    Validate đơn giản: title/artist không rỗng, duration > 0.
    """
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title không được rỗng.")
    if not isinstance(artist, str) or not artist.strip():
        raise ValueError("Artist không được rỗng.")
    try:
        duration_int = int(duration)
    except (ValueError, TypeError):
        raise ValueError("Duration phải là một số nguyên (giây).")
    if duration_int <= 0:
        raise ValueError("Duration phải > 0.")
    song = {'title': title.strip(), 'artist': artist.strip(), 'duration': duration_int}
    songs.append(song)
    return song

def add_song_cli():
    """Wrapper để nhập từ CLI và gọi add_song"""
    try:
        title = input("Nhập tên bài hát: ").strip()
        artist = input("Nhập tên ca sĩ: ").strip()
        duration_raw = input("Nhập thời lượng (giây): ").strip()
        song = add_song(title, artist, duration_raw)
        print(f"Đã thêm: {song['title']} - {song['artist']} ({song['duration']}s)")
    except Exception as e:
        print("Lỗi:", e)
def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '1':
            add_song_cli()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    main()