# 使用streamlit建立網頁, 並且將隱私權政策內容(txet)放入網頁中


import streamlit as st


def app():
    privacy_policy = """
    ## Privacy Policy

    This privacy policy aims to explain how we collect, store, protect, use, and disclose your personal information. By using our app, you are agreeing to this privacy policy.

    ### 1. Information We Collect

    We do not actively collect your personal information. However, we may collect non-personal information about usage of the app, such as features used and frequency of use.

    ### 2. Children's Privacy

    Our app is designed for children and we respect their privacy. We do not actively collect personal information from children.

    ### 3. Use of Information

    We use the information collected to improve our app, to provide a better experience for our users, to improve our products, and to understand user needs.

    ### 4. Disclosure of Information

    We will not disclose your information to any third parties.

    ### 5. Security

    We are committed to ensuring the security of your information. We will take reasonable precautions to protect your information from unauthorized access and processing.

    ### 6. Changes

    We may occasionally update this privacy policy, with updates being posted on our app.

    ### 7. Contact Us

    If you have any questions about this privacy policy, you can contact us at [marsloving43@gmail.com].

    Date: [2023-05-27]
    """

    st.markdown(privacy_policy)


if __name__ == "__main__":
    app()
