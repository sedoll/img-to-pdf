from PIL import Image
import os
import re

def images_to_pdf(folder_path, output_pdf):
    # 지원하는 이미지 확장자
    image_extensions = {"jpg", "jpeg", "png"}
    
    # 폴더 내 이미지 파일 목록 가져오기
    image_files = [f for f in os.listdir(folder_path) if f.split(".")[-1].lower() in image_extensions]
    
    # 파일 이름의 숫자를 기준으로 정렬
    image_files.sort(key=lambda x: [int(num) if num.isdigit() else num for num in re.findall(r'\d+|\D+', x)])
    
    if not image_files:
        print("이미지 파일이 없습니다.")
        return
    
    # 첫 번째 이미지를 기준으로 PDF 생성
    image_list = []
    for image_file in image_files:
        img_path = os.path.join(folder_path, image_file)
        img = Image.open(img_path).convert("RGB")  # PNG 투명도 제거
        image_list.append(img)
    
    # 첫 번째 이미지를 기준으로 PDF 저장
    image_list[0].save(output_pdf, save_all=True, append_images=image_list[1:])
    print(f"PDF 저장 완료: {output_pdf}")

# 예제 사용법
for i in range(4, 15):
    file_name = f"파일 이름 {i:02d}"  # 01, 02, ..., 14 형식 유지
    folder_path = f"./{file_name}"  # 변환할 이미지가 있는 폴더
    output_pdf = f"{file_name}.pdf"  # 저장할 PDF 파일명
    images_to_pdf(folder_path, output_pdf)