import streamlit as st
import requests
import pandas as pd
import os

API_URL = os.environ.get("API_URL")  # Thay đổi URL của API nếu cần

def register_user(name, email, image):
    # Gửi yêu cầu POST đến API để đăng ký người dùng
    response = requests.post(
        f"{API_URL}/users/",
        data={"name": name, "email": email},
        files={"upload_img": image}
    )
    return response.json()

def display_user_info(name, image):
    st.sidebar.title("Thông tin người dùng")
    st.sidebar.image(image, width=250)
    st.sidebar.markdown(
        f'<div style="display: flex; align-items: center; justify-content: center;"><b> {name}</b></div>',
        unsafe_allow_html=True
    )

def get_registered_users():
    # Gửi yêu cầu GET đến API để lấy danh sách người dùng đã đăng ký
    response = requests.get(f"{API_URL}/users/")
    users = response.json()
    return users

def main():
    st.title("Đăng ký tài khoản")

    name = st.text_input("Họ và tên")
    email = st.text_input("Email")
    image = st.file_uploader("Chọn ảnh đại diện", type=["jpg", "jpeg"])

    if st.button("Đăng ký"):
        if not name or not email or not image:
            st.error("Vui lòng điền đầy đủ thông tin và chọn ảnh đại diện.")
        else:
            result = register_user(name, email, image)
            if "message" in result:
                st.success(result["message"])
                # Hiển thị thông tin người dùng trên trang mới
                display_user_info(name, image)

    # Hiển thị danh sách người dùng đã đăng ký
    st.title("Danh sách người dùng đã đăng ký")
    users = get_registered_users()
    df = pd.DataFrame(users)

# Hiển thị dataframe trong một container
    with st.container():
        for index, row in df.iterrows():
            # Tạo một khung cho mỗi người dùng
            with st.expander(f"Người dùng: {row['name']}"):
                # st.image(row['image'], width=100)
                img_user_link = f"{API_URL}/{row['image']}"
                st.image(img_user_link, width=100)
                st.write(f"ID: {row['id']}")
                st.write(f"Email: {row['email']}")


if __name__ == "__main__":
    main()
