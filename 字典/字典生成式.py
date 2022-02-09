# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月28日
"""

#基本格式：{ key_expr: value_expr for value in collection if condition }


temp =  '_octo=GH1.1.1748836919.1635349586; tz=Asia%2FShanghai; _device_id=8b97f43e0b56967dbe3289eadba3d698; user_session=mDF1cCg4jzJ7BK3K1ePbFfUbggerRrXrsZI5eAvo4sxmbWHZ; __Host-user_session_same_site=mDF1cCg4jzJ7BK3K1ePbFfUbggerRrXrsZI5eAvo4sxmbWHZ; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=chengminhua; has_recent_activity=1; _gh_sess=x6aL79RUiSHrzFi0%2F%2Bj3FkwKLmCvlb1L7A6IorIclmF9WcJlGhapYqp38U8YGnsRW8roW5Kt17HK0Qd50U3jEJtXAWJKpoNoHdmTVQ7OugRDmirpAQ8rt0x21nSN7lR09CIE2DSPy%2BSOZOh7yJzWi2Kgfl4qQzMIbmfqKRLTVhu2IcmCwyALafWU0mtZObc0TsiYTppgN0vhqy6pVwayHVlYtExbVDA2WLPw8Q3PpJF%2BOmNzheRW69C8gctbZsTZ4LyGxANxC%2BOqzXCC9Y4%2FVumH%2Bzffm9HGcZ5P0zPnuXjrZmAZTu4yCuXWhhbk4g7VnAMb1Hf1HMGGfwXCapip%2BUEI4Oa7v7TskYPllqhSl5QPjyS0wIKUJ4CPeadUAFU%2Be5l0mc2DcMBEWyTXvpSSqFRQiIosWIQMb8%2BEZP%2B4CEErNZgIUPdH6Zgh%2BpGueF7POILarMlSatbGG8na2NXM%2Bm7nBlY6KMWtxsRU8SOymYZUhBWrk7XxDVvA%2BAgyDghfg3cvvgfxtPwOiPXV8Rk6PHE9EluOhc56HezmYTXF3NsSeDx9LktwoWRT43flivpwwkN9sagxZvmaLeRSssH%2FJJ8uC8mA6r3EOMfaTaqKvtEOnYkGL0Hde83trGfnxAISMRdTDkrttnW5p5Ifq8pB3C0mcPnUa%2FxFror7LOBH4O9PJzHvzMezEqceSeU%3D--7yBomYdG%2F5QvEZyc--q3i2m7eJtEvTyS4IV%2B25QA%3D%3D'

cookie_list = temp.split(';')
cookies = {cookie.split('=')[0]:cookie.split('=')[-1] for cookie in cookie_list}