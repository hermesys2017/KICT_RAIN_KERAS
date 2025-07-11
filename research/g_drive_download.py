import gdown

# 제공된 구글 드라이브 링크
url = "https://drive.google.com/file/d/1F94iWjoUYzWXfvP1-sDuYlOfSdNJFPN7/view?usp=drive_link"

# 파일 ID 추출 (URL에서 파일 ID 부분만 추출)
file_id = url.split("/")[-2]

# 다운로드할 파일 경로 지정 (현재 디렉토리에 원본 파일명으로 저장)
output_path = "downloaded_file.zip"  # 실제 확장자에 맞게 변경하세요

# 파일 다운로드
gdown.download(id=file_id, output=output_path, quiet=False)

print(f"파일이 성공적으로 다운로드되었습니다: {output_path}")
