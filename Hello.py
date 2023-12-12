# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Find the Largest Number",
        page_icon="👋",
    )

    st.write("# Enter 3 Numbers")

    n1 = st.number_input('Enter first number: ')
    n2 = st.number_input('Enter second number: ')
    n3 = st.number_input('Enter third number: ')
    
    mx = max([n1, n2, n3])

    st.write(f"## The largest number is **{mx}**")

    st.write("(this app is created by _Suman Barick_)")



if __name__ == "__main__":
    run()
