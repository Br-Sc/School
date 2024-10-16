from time import sleep

def aggregate_scores(*lists):
    score_dict = {}

    for score_list in lists:
        for entry in score_list.strip().split('\n'):
            # Check if the entry contains ", score: "
            if ", score: " in entry:
                # Split the entry to extract the name and score
                name, score_str = entry.rsplit(", score: ", 1)
                try:
                    score = float(score_str.strip())  # Convert the score to float
                except ValueError:
                    print(f"Could not convert score to float: {score_str}")
                    continue  # Skip to the next entry if conversion fails
                
                # Get the base name (excluding the part from the filename)
                base_name = " ".join(name.split()[:-1])  # Exclude the last part after the last space

                # Aggregate the scores per base name
                if base_name in score_dict:
                    score_dict[base_name] += score
                else:
                    score_dict[base_name] = score
            else:
                print(f"Skipping invalid entry: {entry}")
                sleep(0.4)

    return score_dict


def print_scores(score_dict):
    for name, total_score in score_dict.items():
        print(f"{name}: {total_score:.2f}")


# Example usage with multiple lists
list1 = """
1. rene gerardus nicolaas claasens links_part_1.png, score: 1922.1898636072874
2. merel elisabeth schooneveld links_part_1.png, score: 1943.417697250843
3. roger de jager links_part_1.png, score: 1945.3772560209036
4. rene gerardus nicolaas claasens rechts_part_1.png, score: 1966.452434360981
5. lars sanders links_part_1.png, score: 1966.6932746618986
6. roger de jager rechts_part_1.png, score: 1970.428392574191
7. lars sanders links_part_2.png, score: 1971.3582858741283
8. merel elisabeth schooneveld rechts_part_1.png, score: 1972.1349038928747
9. maria johanna helder links_part_1.png, score: 1973.585802897811
10. tobar yoska rechts_part_1.png, score: 1974.2087117731571
11. jolien marit sanders van opdam links_part_1.png, score: 1979.2548862695694
12. lars sanders rechts_part_1.png, score: 1983.0695137679577
13. tobar yoska links_part_1.png, score: 1987.52608191967
14. katie anne schipper rechts_part_1.png, score: 1989.1195470839739
15. lars sanders rechts_part_2.png, score: 1999.5733236521482
16. jolien marit sanders van opdam rechts_part_1.png, score: 1999.7491748034954
17. rene gerardus nicolaas claasens rechts_part_2.png, score: 2004.4162517040968
18. lars sanders rechts_part_4.png, score: 2009.3957494795322
19. tobar yoska rechts_part_2.png, score: 2018.1809019446373
20. maria johanna helder links_part_2.png, score: 2019.0424638688564
21. maria johanna helder rechts_part_1.png, score: 2021.9517755955458
22. katie anne schipper links_part_1.png, score: 2022.8618849813938
23. jolien marit sanders van opdam links_part_3.png, score: 2026.386853158474
24. egbert adrianus sanders rechts_part_1.png, score: 2031.100992769003
25. rene gerardus nicolaas claasens links_part_2.png, score: 2031.4286519885063
26. tobar yoska links_part_2.png, score: 2034.2371460199356
27. lars sanders rechts_part_3.png, score: 2042.3169035166502
28. jolien marit sanders van opdam links_part_2.png, score: 2045.1355457752943
29. merel elisabeth schooneveld rechts_part_3.png, score: 2046.327989026904
30. maria johanna helder rechts_part_2.png, score: 2047.2066842019558
31. maria johanna helder links_part_3.png, score: 2047.348899334669
32. maria johanna helder rechts_part_3.png, score: 2051.7412668913603
33. jolien marit sanders van opdam rechts_part_4.png, score: 2051.757664695382
34. rene gerardus nicolaas claasens links_part_3.png, score: 2056.5227124989033
35. katie anne schipper rechts_part_2.png, score: 2056.8451563566923
36. merel elisabeth schooneveld links_part_3.png, score: 2056.942940235138
37. tobar yoska rechts_part_3.png, score: 2058.3435065597296
38. merel elisabeth schooneveld links_part_2.png, score: 2059.5300082564354
39. rene gerardus nicolaas claasens rechts_part_3.png, score: 2065.4391932934523
40. robert vink rechts_part_1.png, score: 2065.9793817847967
41. lars sanders links_part_3.png, score: 2067.2271835654974
42. merel elisabeth schooneveld rechts_part_2.png, score: 2070.0429599434137
43. rachel janssen rechts_part_1.png, score: 2073.37841527164
44. roger de jager links_part_3.png, score: 2077.306134879589
45. huub cornelius henselmans links_part_1.png, score: 2078.3661276996136
46. katie anne schipper links_part_2.png, score: 2082.665060982108
47. tobar yoska links_part_5.png, score: 2089.384965389967
48. huub cornelius henselmans rechts_part_1.png, score: 2093.7384609133005
49. jolien marit sanders van opdam rechts_part_3.png, score: 2093.9405040740967
50. rachel janssen links_part_1.png, score: 2094.357032954693
51. merel elisabeth schooneveld links_part_4.png, score: 2094.670786291361
52. roger de jager rechts_part_2.png, score: 2095.926989674568
53. egbert adrianus sanders links_part_1.png, score: 2097.1413554251194
54. merel elisabeth schooneveld rechts_part_4.png, score: 2098.744671076536
55. jolien marit sanders van opdam links_part_4.png, score: 2100.2327522039413
56. robert vink links_part_1.png, score: 2101.699547678232
57. tobar yoska links_part_3.png, score: 2101.9334146380424
58. rene gerardus nicolaas claasens links_part_4.png, score: 2102.0526470541954
59. roger de jager links_part_2.png, score: 2104.619198769331
60. huub cornelius henselmans rechts_part_3.png, score: 2106.604715883732
61. jolien marit sanders van opdam rechts_part_2.png, score: 2108.342396095395
62. lars sanders links_part_4.png, score: 2110.743756607175
63. maria johanna helder rechts_part_4.png, score: 2110.9319473206997
64. hannah catharina hoogendoorn rechts_part_2.png, score: 2111.2310743778944
65. rachel janssen rechts_part_3.png, score: 2112.065499588847
66. katie anne schipper links_part_3.png, score: 2117.297145470977
67. jolien marit sanders van opdam rechts_part_5.png, score: 2119.373904019594
68. rachel janssen links_part_2.png, score: 2120.533279940486
69. tobar yoska rechts_part_5.png, score: 2121.3014805316925
70. egbert adrianus sanders rechts_part_3.png, score: 2126.3009914159775
71. tobar yoska links_part_4.png, score: 2127.014822334051
72. roger de jager links_part_4.png, score: 2127.0833161324263
73. egbert adrianus sanders rechts_part_2.png, score: 2141.4466085135937
74. rachel janssen links_part_3.png, score: 2142.7376978993416
75. robert vink links_part_4.png, score: 2143.697586670518
76. jolien marit sanders van opdam links_part_5.png, score: 2147.5293052494526
77. rachel janssen rechts_part_2.png, score: 2149.8491795659065
78. robert vink rechts_part_2.png, score: 2151.657164543867
79. roger de jager rechts_part_3.png, score: 2157.521185040474
80. robert vink links_part_2.png, score: 2167.309206739068
81. huub cornelius henselmans rechts_part_2.png, score: 2168.513654589653
82. maria johanna helder links_part_4.png, score: 2175.1493203043938
83. robert vink rechts_part_4.png, score: 2176.123319029808
84. merel elisabeth schooneveld links_part_5.png, score: 2176.851677402854
85. hannah catharina hoogendoorn rechts_part_1.png, score: 2179.0704098641872
86. katie anne schipper rechts_part_3.png, score: 2179.9348419606686
87. egbert adrianus sanders links_part_2.png, score: 2181.9699837863445
88. maria johanna helder rechts_part_5.png, score: 2183.0159359276295
89. roger de jager links_part_5.png, score: 2183.566753447056
90. egbert adrianus sanders rechts_part_4.png, score: 2183.6344357579947
91. robert vink links_part_3.png, score: 2185.4070498645306
92. robert vink rechts_part_3.png, score: 2185.4180398881435
93. roger de jager rechts_part_4.png, score: 2189.5833443552256
94. egbert adrianus sanders links_part_3.png, score: 2192.414628893137
95. lars sanders rechts_part_5.png, score: 2193.830170482397
96. katie anne schipper links_part_5.png, score: 2196.39729398489
97. rene gerardus nicolaas claasens links_part_5.png, score: 2198.809871315956
98. katie anne schipper links_part_4.png, score: 2204.1004895865917
99. merel elisabeth schooneveld rechts_part_5.png, score: 2209.150090113282
100. lars sanders links_part_5.png, score: 2209.926310479641
101. hannah catharina hoogendoorn rechts_part_3.png, score: 2216.373958989978
102. katie anne schipper rechts_part_4.png, score: 2220.345500290394
103. maria johanna helder links_part_5.png, score: 2226.3883590996265
104. huub cornelius henselmans links_part_2.png, score: 2231.11423099041
105. robert vink links_part_5.png, score: 2242.2628738880157
106. rene gerardus nicolaas claasens rechts_part_4.png, score: 2244.2542925179005
107. katie anne schipper rechts_part_5.png, score: 2244.312023639679
108. robert vink rechts_part_5.png, score: 2248.1808222532272
109. huub cornelius henselmans links_part_3.png, score: 2256.8169768452644
110. rachel janssen links_part_5.png, score: 2275.9571416974068
111. huub cornelius henselmans rechts_part_4.png, score: 2279.551599264145
112. hannah catharina hoogendoorn links_part_2.png, score: 2283.855678796768
113. huub cornelius henselmans rechts_part_5.png, score: 2284.82512126863
114. rachel janssen rechts_part_5.png, score: 2316.7283005714417
115. roger de jager rechts_part_5.png, score: 2319.7550341188908
116. tobar yoska rechts_part_4.png, score: 2325.0917191803455
117. rene gerardus nicolaas claasens rechts_part_5.png, score: 2331.891038298607
118. rachel janssen links_part_4.png, score: 2332.764815479517
119. hannah catharina hoogendoorn links_part_5.png, score: 2352.579250305891
120. huub cornelius henselmans links_part_4.png, score: 2368.6976007819176
121. hannah catharina hoogendoorn links_part_1.png, score: 2380.2459677755833
122. egbert adrianus sanders rechts_part_5.png, score: 2384.0195898115635
123. egbert adrianus sanders links_part_4.png, score: 2388.5873213410378
124. hannah catharina hoogendoorn links_part_4.png, score: 2399.8047480881214
125. rachel janssen rechts_part_4.png, score: 2437.677738070488
126. hannah catharina hoogendoorn links_part_3.png, score: 2457.984011977911
127. huub cornelius henselmans links_part_5.png, score: 2461.8282427191734
128. hannah catharina hoogendoorn rechts_part_4.png, score: 2505.2346884310246
129. egbert adrianus sanders links_part_5.png, score: 2537.721493303776
130. hannah catharina hoogendoorn rechts_part_5.png, score: 2588.93468734622
"""

list2 = """
1. rene gerardus nicolaas claasens links_part_1.png, score: 1582.0188100636005
2. merel elisabeth schooneveld links_part_1.png, score: 1589.5765222012997
3. roger de jager links_part_1.png, score: 1597.8684955090284
4. lars sanders links_part_1.png, score: 1608.826193496585
5. merel elisabeth schooneveld rechts_part_1.png, score: 1616.1980089843273
6. lars sanders links_part_2.png, score: 1622.4502928256989
7. tobar yoska rechts_part_1.png, score: 1626.7134073376656
8. jolien marit sanders van opdam links_part_1.png, score: 1630.092352166772
9. katie anne schipper rechts_part_1.png, score: 1633.199955612421
10. maria johanna helder links_part_1.png, score: 1635.9805146157742
11. rene gerardus nicolaas claasens rechts_part_1.png, score: 1637.670198842883
12. roger de jager rechts_part_1.png, score: 1638.463668167591
13. jolien marit sanders van opdam rechts_part_1.png, score: 1642.9090724140406
14. tobar yoska links_part_1.png, score: 1644.8323709070683
15. lars sanders rechts_part_2.png, score: 1649.250230833888
16. lars sanders rechts_part_1.png, score: 1657.6266154497862
17. rene gerardus nicolaas claasens rechts_part_2.png, score: 1661.5130899846554
18. maria johanna helder links_part_2.png, score: 1670.521259188652
19. lars sanders rechts_part_4.png, score: 1673.4430493861437
20. katie anne schipper links_part_1.png, score: 1673.5861744582653
21. jolien marit sanders van opdam links_part_3.png, score: 1677.1657923012972
22. tobar yoska rechts_part_2.png, score: 1678.3429629206657
23. katie anne schipper rechts_part_2.png, score: 1680.494859725237
24. tobar yoska links_part_2.png, score: 1683.3764716535807
25. jolien marit sanders van opdam links_part_2.png, score: 1689.0878079980612
26. egbert adrianus sanders rechts_part_1.png, score: 1689.7033830434084
27. merel elisabeth schooneveld rechts_part_3.png, score: 1689.7711531370878
28. jolien marit sanders van opdam rechts_part_4.png, score: 1693.254960000515
29. tobar yoska rechts_part_3.png, score: 1698.290086582303
30. robert vink rechts_part_1.png, score: 1700.3612038493156
31. rene gerardus nicolaas claasens links_part_2.png, score: 1701.441420957446
32. merel elisabeth schooneveld rechts_part_2.png, score: 1701.9852777570486
33. lars sanders links_part_3.png, score: 1705.0459919422865
34. maria johanna helder links_part_3.png, score: 1705.1330803632736
35. maria johanna helder rechts_part_2.png, score: 1706.96152792871
36. lars sanders rechts_part_3.png, score: 1709.7435734570026
37. katie anne schipper links_part_2.png, score: 1711.1233439743519
38. merel elisabeth schooneveld links_part_2.png, score: 1714.150544822216
39. rene gerardus nicolaas claasens links_part_3.png, score: 1715.375161215663
40. maria johanna helder rechts_part_3.png, score: 1715.6659934669733
41. maria johanna helder rechts_part_1.png, score: 1715.945674866438
42. merel elisabeth schooneveld links_part_3.png, score: 1723.1557722240686
43. jolien marit sanders van opdam rechts_part_3.png, score: 1723.897593691945
44. roger de jager links_part_3.png, score: 1724.9189679324627
45. tobar yoska rechts_part_5.png, score: 1731.7824469953775
46. rachel janssen rechts_part_1.png, score: 1732.5445227771997
47. egbert adrianus sanders links_part_1.png, score: 1732.8105229884386
48. robert vink links_part_1.png, score: 1735.456704750657
49. rene gerardus nicolaas claasens rechts_part_3.png, score: 1738.5102255046368
50. jolien marit sanders van opdam rechts_part_2.png, score: 1739.5848792493343
51. roger de jager rechts_part_2.png, score: 1747.5369576066732
52. roger de jager links_part_2.png, score: 1748.8138487935066
53. tobar yoska links_part_5.png, score: 1749.792548134923
54. rachel janssen rechts_part_3.png, score: 1750.453216969967
55. huub cornelius henselmans links_part_1.png, score: 1750.8032978624105
56. huub cornelius henselmans rechts_part_1.png, score: 1754.0177931189537
57. merel elisabeth schooneveld rechts_part_4.png, score: 1754.807003378868
58. jolien marit sanders van opdam links_part_4.png, score: 1754.9864730536938
59. huub cornelius henselmans rechts_part_3.png, score: 1756.9786029607058
60. katie anne schipper links_part_3.png, score: 1758.076111793518
61. tobar yoska links_part_3.png, score: 1759.82532954216
62. merel elisabeth schooneveld links_part_4.png, score: 1760.2038805484772
63. hannah catharina hoogendoorn rechts_part_2.png, score: 1762.3160612881184
64. rachel janssen links_part_1.png, score: 1766.6607219278812
65. lars sanders links_part_4.png, score: 1770.3908648490906
66. robert vink rechts_part_2.png, score: 1771.2792048603296
67. jolien marit sanders van opdam rechts_part_5.png, score: 1777.7546527683735
68. rene gerardus nicolaas claasens links_part_4.png, score: 1779.914806202054
69. maria johanna helder rechts_part_4.png, score: 1782.6275634169579
70. roger de jager links_part_4.png, score: 1785.3123869746923
71. rachel janssen links_part_2.png, score: 1786.6597784906626
72. egbert adrianus sanders rechts_part_3.png, score: 1788.8587097972631
73. robert vink links_part_4.png, score: 1790.4104059785604
74. egbert adrianus sanders rechts_part_2.png, score: 1794.6189756542444
75. rachel janssen rechts_part_2.png, score: 1795.1370423585176
76. tobar yoska links_part_4.png, score: 1795.9912081956863
77. robert vink links_part_2.png, score: 1796.6386517435312
78. rachel janssen links_part_3.png, score: 1801.10367462039
79. robert vink rechts_part_4.png, score: 1804.0937843173742
80. robert vink rechts_part_3.png, score: 1812.394178017974
81. jolien marit sanders van opdam links_part_5.png, score: 1815.7306558787823
82. huub cornelius henselmans rechts_part_2.png, score: 1828.98386195302
83. merel elisabeth schooneveld links_part_5.png, score: 1833.929019600153
84. roger de jager rechts_part_3.png, score: 1836.7210592627525
85. egbert adrianus sanders rechts_part_4.png, score: 1837.5557188987732
86. katie anne schipper rechts_part_3.png, score: 1838.1425177156925
87. egbert adrianus sanders links_part_2.png, score: 1839.179566591978
88. katie anne schipper links_part_5.png, score: 1841.3978961110115
89. maria johanna helder links_part_4.png, score: 1842.935741752386
90. roger de jager rechts_part_4.png, score: 1845.367751389742
91. maria johanna helder rechts_part_5.png, score: 1853.0349846333265
92. robert vink links_part_3.png, score: 1854.8365806043148
93. roger de jager links_part_5.png, score: 1855.0105590224266
94. katie anne schipper links_part_4.png, score: 1855.3624017089605
95. merel elisabeth schooneveld rechts_part_5.png, score: 1860.8284177035093
96. katie anne schipper rechts_part_4.png, score: 1860.843164756894
97. lars sanders rechts_part_5.png, score: 1866.067869901657
98. egbert adrianus sanders links_part_3.png, score: 1867.6804826408625
99. hannah catharina hoogendoorn rechts_part_3.png, score: 1873.6710183620453
100. lars sanders links_part_5.png, score: 1878.938863813877
101. hannah catharina hoogendoorn rechts_part_1.png, score: 1879.8614536076784
102. rene gerardus nicolaas claasens links_part_5.png, score: 1880.0187757015228
103. robert vink rechts_part_5.png, score: 1885.1376377791166
104. katie anne schipper rechts_part_5.png, score: 1895.016714721918
105. huub cornelius henselmans links_part_2.png, score: 1895.5297794044018
106. robert vink links_part_5.png, score: 1899.920615553856
107. maria johanna helder links_part_5.png, score: 1905.1560362279415
108. rene gerardus nicolaas claasens rechts_part_4.png, score: 1935.792038321495
109. huub cornelius henselmans links_part_3.png, score: 1943.617633074522
110. hannah catharina hoogendoorn links_part_2.png, score: 1956.3236501812935
111. huub cornelius henselmans rechts_part_5.png, score: 1960.3531368672848
112. rachel janssen links_part_5.png, score: 1967.1240901350975
113. rachel janssen rechts_part_5.png, score: 1975.169803082943
114. huub cornelius henselmans rechts_part_4.png, score: 1978.4041203856468
115. tobar yoska rechts_part_4.png, score: 1991.6881904900074
116. rachel janssen links_part_4.png, score: 1995.9642060995102
117. roger de jager rechts_part_5.png, score: 2009.5973483622074
118. rene gerardus nicolaas claasens rechts_part_5.png, score: 2033.5584789812565
119. hannah catharina hoogendoorn links_part_5.png, score: 2051.9184947907925
120. huub cornelius henselmans links_part_4.png, score: 2069.164107054472
121. egbert adrianus sanders rechts_part_5.png, score: 2073.717140465975
122. egbert adrianus sanders links_part_4.png, score: 2081.503272384405
123. hannah catharina hoogendoorn links_part_4.png, score: 2093.0637062191963
124. hannah catharina hoogendoorn links_part_1.png, score: 2103.5206486284733
125. rachel janssen rechts_part_4.png, score: 2145.827370405197
126. huub cornelius henselmans links_part_5.png, score: 2157.72267511487
127. hannah catharina hoogendoorn links_part_3.png, score: 2198.3871373534203
128. hannah catharina hoogendoorn rechts_part_4.png, score: 2212.846877515316
129. egbert adrianus sanders links_part_5.png, score: 2245.1618920862675
130. hannah catharina hoogendoorn rechts_part_5.png, score: 2277.3440218269825
"""

list3 = """
1. roger de jager links_part_1.png, score: 1572.6740885227919
2. rene gerardus nicolaas claasens links_part_1.png, score: 1575.608415812254
3. merel elisabeth schooneveld links_part_1.png, score: 1589.7443565577269
4. lars sanders links_part_1.png, score: 1590.9956650137901
5. jolien marit sanders van opdam links_part_1.png, score: 1604.4697015732527
6. merel elisabeth schooneveld rechts_part_1.png, score: 1615.3672596365213
7. lars sanders links_part_2.png, score: 1619.3301118016243
8. tobar yoska rechts_part_1.png, score: 1619.6026395261288
9. maria johanna helder links_part_1.png, score: 1620.5050373375416
10. katie anne schipper rechts_part_1.png, score: 1622.4229667186737
11. rene gerardus nicolaas claasens rechts_part_1.png, score: 1623.1650107055902
12. jolien marit sanders van opdam rechts_part_1.png, score: 1623.9845910966396
13. roger de jager rechts_part_1.png, score: 1624.6748604923487
14. lars sanders rechts_part_1.png, score: 1625.2145830392838
15. tobar yoska links_part_1.png, score: 1630.5603735595942
16. tobar yoska links_part_2.png, score: 1640.2094490379095
17. tobar yoska rechts_part_2.png, score: 1644.208709821105
18. lars sanders rechts_part_2.png, score: 1644.3567807078362
19. lars sanders rechts_part_4.png, score: 1644.8218047320843
20. katie anne schipper links_part_1.png, score: 1646.5213663876057
21. jolien marit sanders van opdam links_part_3.png, score: 1647.0886206179857
22. maria johanna helder links_part_2.png, score: 1649.5006209760904
23. rene gerardus nicolaas claasens rechts_part_2.png, score: 1650.4209150522947
24. jolien marit sanders van opdam rechts_part_4.png, score: 1659.7178964018822
25. egbert adrianus sanders rechts_part_1.png, score: 1660.0982942432165
26. maria johanna helder rechts_part_1.png, score: 1663.66466152668
27. jolien marit sanders van opdam links_part_2.png, score: 1667.2636621147394
28. merel elisabeth schooneveld rechts_part_3.png, score: 1667.7810254991055
29. katie anne schipper rechts_part_2.png, score: 1674.0930263102055
30. rene gerardus nicolaas claasens links_part_2.png, score: 1674.845059260726
31. tobar yoska rechts_part_3.png, score: 1675.8173966556787
32. maria johanna helder rechts_part_2.png, score: 1676.4276599735022
33. maria johanna helder links_part_3.png, score: 1677.7003133744001
34. maria johanna helder rechts_part_3.png, score: 1677.705172330141
35. robert vink rechts_part_1.png, score: 1678.1624381393194
36. merel elisabeth schooneveld links_part_3.png, score: 1679.7562872767448
37. roger de jager links_part_3.png, score: 1680.0267909169197
38. merel elisabeth schooneveld rechts_part_2.png, score: 1682.0087744742632
39. lars sanders rechts_part_3.png, score: 1682.9834158420563
40. merel elisabeth schooneveld links_part_2.png, score: 1686.0303542613983
41. rene gerardus nicolaas claasens rechts_part_3.png, score: 1689.7842520177364
42. rachel janssen rechts_part_1.png, score: 1692.346590474248
43. katie anne schipper links_part_2.png, score: 1692.6737056225538
44. lars sanders links_part_3.png, score: 1692.7975360006094
45. jolien marit sanders van opdam rechts_part_3.png, score: 1694.9029326587915
46. rene gerardus nicolaas claasens links_part_3.png, score: 1697.2230360656977
47. egbert adrianus sanders links_part_1.png, score: 1700.1385855823755
48. robert vink links_part_1.png, score: 1700.6936204582453
49. jolien marit sanders van opdam links_part_4.png, score: 1701.5133681595325
50. merel elisabeth schooneveld rechts_part_4.png, score: 1706.6435338556767
51. merel elisabeth schooneveld links_part_4.png, score: 1707.3048490732908
52. rachel janssen links_part_1.png, score: 1709.7299945354462
53. huub cornelius henselmans links_part_1.png, score: 1709.8193819373846
54. roger de jager rechts_part_2.png, score: 1710.1825962513685
55. lars sanders links_part_4.png, score: 1713.7755218595266
56. rachel janssen rechts_part_3.png, score: 1714.046214580536
57. jolien marit sanders van opdam rechts_part_2.png, score: 1714.2749709188938
58. huub cornelius henselmans rechts_part_3.png, score: 1714.3788268864155
59. roger de jager links_part_2.png, score: 1715.662338271737
60. maria johanna helder rechts_part_4.png, score: 1715.9477033168077
61. katie anne schipper links_part_3.png, score: 1716.7453847825527
62. huub cornelius henselmans rechts_part_1.png, score: 1718.432837292552
63. jolien marit sanders van opdam rechts_part_5.png, score: 1719.1121549457312
64. tobar yoska links_part_5.png, score: 1722.696206241846
65. rene gerardus nicolaas claasens links_part_4.png, score: 1724.1859404593706
66. roger de jager links_part_4.png, score: 1728.7579792290926
67. robert vink links_part_4.png, score: 1730.3529057055712
68. tobar yoska rechts_part_5.png, score: 1730.625803500414
69. hannah catharina hoogendoorn rechts_part_2.png, score: 1733.6157990694046
70. egbert adrianus sanders rechts_part_3.png, score: 1733.8551036715508
71. tobar yoska links_part_3.png, score: 1735.8388576358557
72. rachel janssen links_part_3.png, score: 1740.0642358064651
73. egbert adrianus sanders rechts_part_2.png, score: 1741.1313722282648
74. rachel janssen links_part_2.png, score: 1741.8718141913414
75. robert vink rechts_part_2.png, score: 1747.3343359827995
76. rachel janssen rechts_part_2.png, score: 1749.5213534832
77. tobar yoska links_part_4.png, score: 1751.513253301382
78. jolien marit sanders van opdam links_part_5.png, score: 1756.6632757782936
79. robert vink links_part_2.png, score: 1760.293416261673
80. merel elisabeth schooneveld links_part_5.png, score: 1761.5615232735872
81. robert vink rechts_part_4.png, score: 1768.260408371687
82. roger de jager rechts_part_3.png, score: 1769.385376304388
83. robert vink rechts_part_3.png, score: 1770.655366241932
84. egbert adrianus sanders rechts_part_4.png, score: 1772.2681225985289
85. roger de jager rechts_part_4.png, score: 1773.0346102714539
86. egbert adrianus sanders links_part_2.png, score: 1779.8817718327045
87. roger de jager links_part_5.png, score: 1780.358174085617
88. katie anne schipper rechts_part_3.png, score: 1780.5831447541714
89. katie anne schipper links_part_5.png, score: 1780.9922559559345
90. maria johanna helder rechts_part_5.png, score: 1783.034455806017
91. maria johanna helder links_part_4.png, score: 1784.5923665463924
92. katie anne schipper links_part_4.png, score: 1785.4623792171478
93. egbert adrianus sanders links_part_3.png, score: 1786.262347906828
94. merel elisabeth schooneveld rechts_part_5.png, score: 1789.891200259328
95. huub cornelius henselmans rechts_part_2.png, score: 1790.8918972313404
96. hannah catharina hoogendoorn rechts_part_1.png, score: 1792.4275852143764
97. katie anne schipper rechts_part_4.png, score: 1794.8796745836735
98. robert vink links_part_3.png, score: 1798.0521368384361
99. lars sanders rechts_part_5.png, score: 1804.0011818110943
100. hannah catharina hoogendoorn rechts_part_3.png, score: 1807.921218752861
101. rene gerardus nicolaas claasens links_part_5.png, score: 1810.3824327588081
102. robert vink rechts_part_5.png, score: 1813.7103154212236
103. lars sanders links_part_5.png, score: 1814.1347960829735
104. robert vink links_part_5.png, score: 1826.0162588655949
105. huub cornelius henselmans links_part_2.png, score: 1826.508656591177
106. katie anne schipper rechts_part_5.png, score: 1827.0304886698723
107. maria johanna helder links_part_5.png, score: 1832.04555234313
108. rene gerardus nicolaas claasens rechts_part_4.png, score: 1849.838450551033
109. huub cornelius henselmans links_part_3.png, score: 1858.9588354825974
110. rachel janssen links_part_5.png, score: 1869.2073462307453
111. huub cornelius henselmans rechts_part_5.png, score: 1873.6912678480148
112. huub cornelius henselmans rechts_part_4.png, score: 1878.3638933598995
113. hannah catharina hoogendoorn links_part_2.png, score: 1880.168551594019
114. rachel janssen links_part_4.png, score: 1890.010194838047
115. rachel janssen rechts_part_5.png, score: 1892.6255274415016
116. roger de jager rechts_part_5.png, score: 1908.3359852135181
117. rene gerardus nicolaas claasens rechts_part_5.png, score: 1915.0448631942272
118. tobar yoska rechts_part_4.png, score: 1919.6099249124527
119. hannah catharina hoogendoorn links_part_5.png, score: 1936.5439640581608
120. huub cornelius henselmans links_part_4.png, score: 1956.485226213932
121. egbert adrianus sanders rechts_part_5.png, score: 1966.16223102808
122. egbert adrianus sanders links_part_4.png, score: 1967.9692553579807
123. hannah catharina hoogendoorn links_part_1.png, score: 1972.9745263457298
124. hannah catharina hoogendoorn links_part_4.png, score: 1991.471832960844
125. rachel janssen rechts_part_4.png, score: 2006.679490685463
126. huub cornelius henselmans links_part_5.png, score: 2018.814871698618
127. hannah catharina hoogendoorn links_part_3.png, score: 2033.625476449728
128. hannah catharina hoogendoorn rechts_part_4.png, score: 2072.701354265213
129. egbert adrianus sanders links_part_5.png, score: 2081.489371865988
130. hannah catharina hoogendoorn rechts_part_5.png, score: 2132.0925664007664
"""

list4 = """
1. jolien marit sanders van opdam links_part_1.png, score: 3486.4643290042877
2. lars sanders links_part_1.png, score: 3489.421381622553
3. roger de jager links_part_1.png, score: 3539.1143359690905
4. merel elisabeth schooneveld links_part_1.png, score: 3564.431706741452
5. tobar yoska rechts_part_1.png, score: 3570.724254667759
6. rene gerardus nicolaas claasens links_part_1.png, score: 3571.524991720915
7. merel elisabeth schooneveld rechts_part_1.png, score: 3579.5634693205357
8. jolien marit sanders van opdam rechts_part_1.png, score: 3603.759499847889
9. tobar yoska links_part_1.png, score: 3612.325553536415
10. maria johanna helder links_part_1.png, score: 3614.447335615754
11. tobar yoska links_part_2.png, score: 3615.0336036086082
12. katie anne schipper rechts_part_1.png, score: 3617.341314136982
13. lars sanders links_part_2.png, score: 3627.771895572543
14. lars sanders rechts_part_1.png, score: 3647.790937781334
15. jolien marit sanders van opdam links_part_3.png, score: 3657.740183517337
16. roger de jager rechts_part_1.png, score: 3661.22215898335
17. tobar yoska rechts_part_3.png, score: 3666.0069938600063
18. katie anne schipper links_part_1.png, score: 3673.453262746334
19. tobar yoska rechts_part_2.png, score: 3678.1912827044725
20. merel elisabeth schooneveld links_part_3.png, score: 3678.4287947267294
21. maria johanna helder links_part_2.png, score: 3683.1721720844507
22. rene gerardus nicolaas claasens rechts_part_1.png, score: 3684.1368391364813
23. jolien marit sanders van opdam links_part_2.png, score: 3684.549846455455
24. maria johanna helder links_part_3.png, score: 3686.9426095485687
25. lars sanders rechts_part_2.png, score: 3695.790707230568
26. egbert adrianus sanders rechts_part_1.png, score: 3699.2339847385883
27. merel elisabeth schooneveld rechts_part_3.png, score: 3702.142711251974
28. lars sanders rechts_part_4.png, score: 3709.2193838506937
29. robert vink links_part_1.png, score: 3712.724519342184
30. jolien marit sanders van opdam rechts_part_4.png, score: 3715.2218025177717
31. robert vink rechts_part_1.png, score: 3715.7184134572744
32. rene gerardus nicolaas claasens rechts_part_2.png, score: 3719.4598797112703
33. rachel janssen links_part_1.png, score: 3719.4933757781982
34. maria johanna helder rechts_part_1.png, score: 3731.8323653787374
35. rachel janssen rechts_part_3.png, score: 3733.977018997073
36. maria johanna helder rechts_part_3.png, score: 3734.470595344901
37. roger de jager links_part_3.png, score: 3734.6082303225994
38. maria johanna helder rechts_part_2.png, score: 3737.516378685832
39. katie anne schipper rechts_part_2.png, score: 3749.312718629837
40. rene gerardus nicolaas claasens links_part_2.png, score: 3750.76693610847
41. jolien marit sanders van opdam rechts_part_2.png, score: 3750.9055310338736
42. huub cornelius henselmans rechts_part_3.png, score: 3752.177592560649
43. lars sanders rechts_part_3.png, score: 3757.8352905213833
44. merel elisabeth schooneveld links_part_5.png, score: 3759.5047115385532
45. rachel janssen rechts_part_1.png, score: 3760.691255956888
46. lars sanders links_part_3.png, score: 3767.1074539273977
47. jolien marit sanders van opdam links_part_4.png, score: 3769.014256313443
48. merel elisabeth schooneveld rechts_part_2.png, score: 3770.076783746481
49. katie anne schipper links_part_3.png, score: 3771.356968462467
50. merel elisabeth schooneveld links_part_2.png, score: 3774.2946227937937
51. roger de jager links_part_4.png, score: 3774.7412989139557
52. jolien marit sanders van opdam rechts_part_3.png, score: 3775.21263435483
53. roger de jager rechts_part_2.png, score: 3775.246610239148
54. merel elisabeth schooneveld links_part_4.png, score: 3781.906702876091
55. roger de jager links_part_2.png, score: 3785.869726419449
56. merel elisabeth schooneveld rechts_part_4.png, score: 3787.0487669855356
57. rachel janssen links_part_3.png, score: 3790.6431081593037
58. tobar yoska links_part_5.png, score: 3791.6995942294598
59. katie anne schipper links_part_2.png, score: 3795.3017980605364
60. robert vink links_part_2.png, score: 3799.4558699578047
61. huub cornelius henselmans rechts_part_1.png, score: 3804.2179501503706
62. rene gerardus nicolaas claasens links_part_3.png, score: 3804.825976729393
63. rene gerardus nicolaas claasens rechts_part_3.png, score: 3806.7915980368853
64. jolien marit sanders van opdam rechts_part_5.png, score: 3807.5229607969522
65. egbert adrianus sanders links_part_1.png, score: 3809.1665805727243
66. maria johanna helder rechts_part_4.png, score: 3810.9294628053904
67. huub cornelius henselmans links_part_1.png, score: 3818.363853663206
68. robert vink rechts_part_2.png, score: 3821.926269456744
69. tobar yoska links_part_3.png, score: 3825.2983886748552
70. lars sanders links_part_4.png, score: 3826.379612773657
71. rene gerardus nicolaas claasens links_part_4.png, score: 3829.332159459591
72. tobar yoska rechts_part_5.png, score: 3836.2767959088087
73. robert vink links_part_4.png, score: 3839.458160623908
74. egbert adrianus sanders rechts_part_3.png, score: 3840.442974716425
75. jolien marit sanders van opdam links_part_5.png, score: 3845.3499584943056
76. merel elisabeth schooneveld rechts_part_5.png, score: 3849.911217406392
77. rachel janssen links_part_2.png, score: 3850.4195266216993
78. hannah catharina hoogendoorn rechts_part_2.png, score: 3860.4450242221355
79. rachel janssen rechts_part_2.png, score: 3869.120297431946
80. robert vink rechts_part_4.png, score: 3870.8644157648087
81. maria johanna helder rechts_part_5.png, score: 3871.269945651293
82. katie anne schipper links_part_5.png, score: 3872.039031818509
83. robert vink rechts_part_3.png, score: 3873.0472186505795
84. roger de jager rechts_part_3.png, score: 3881.2445309460163
85. egbert adrianus sanders rechts_part_2.png, score: 3891.640084579587
86. tobar yoska links_part_4.png, score: 3898.630987852812
87. egbert adrianus sanders links_part_2.png, score: 3904.6404406279325
88. roger de jager rechts_part_4.png, score: 3912.7135442197323
89. maria johanna helder links_part_4.png, score: 3917.2082251757383
90. katie anne schipper links_part_4.png, score: 3918.5254184007645
91. hannah catharina hoogendoorn rechts_part_1.png, score: 3928.3962044268847
92. katie anne schipper rechts_part_3.png, score: 3934.5046522170305
93. egbert adrianus sanders rechts_part_4.png, score: 3934.7003878206015
94. hannah catharina hoogendoorn rechts_part_3.png, score: 3935.6702371388674
95. katie anne schipper rechts_part_4.png, score: 3941.212347045541
96. egbert adrianus sanders links_part_3.png, score: 3948.244014889002
97. roger de jager links_part_5.png, score: 3951.2986333072186
98. huub cornelius henselmans links_part_2.png, score: 3954.414728999138
99. robert vink rechts_part_5.png, score: 3955.2121095210314
100. robert vink links_part_5.png, score: 3969.627825498581
101. maria johanna helder links_part_5.png, score: 3970.8954150676727
102. huub cornelius henselmans rechts_part_2.png, score: 4011.67014297843
103. robert vink links_part_3.png, score: 4012.750637665391
104. lars sanders links_part_5.png, score: 4012.7789474725723
105. rene gerardus nicolaas claasens links_part_5.png, score: 4022.7848270088434
106. lars sanders rechts_part_5.png, score: 4042.464206010103
107. katie anne schipper rechts_part_5.png, score: 4046.9480207264423
108. huub cornelius henselmans rechts_part_5.png, score: 4066.539129540324
109. rachel janssen links_part_5.png, score: 4080.3591735064983
110. rachel janssen rechts_part_5.png, score: 4081.9599778950214
111. rene gerardus nicolaas claasens rechts_part_4.png, score: 4082.971719443798
112. huub cornelius henselmans rechts_part_4.png, score: 4089.9607878923416
113. hannah catharina hoogendoorn links_part_2.png, score: 4111.672584146261
114. rachel janssen links_part_4.png, score: 4114.1528432667255
115. huub cornelius henselmans links_part_3.png, score: 4118.636800020933
116. rene gerardus nicolaas claasens rechts_part_5.png, score: 4155.551039844751
117. tobar yoska rechts_part_4.png, score: 4162.385064914823
118. roger de jager rechts_part_5.png, score: 4205.466798096895
119. hannah catharina hoogendoorn links_part_5.png, score: 4226.561778247356
120. egbert adrianus sanders rechts_part_5.png, score: 4330.181407541037
121. egbert adrianus sanders links_part_4.png, score: 4333.54371291399
122. hannah catharina hoogendoorn links_part_1.png, score: 4349.3931794166565
123. rachel janssen rechts_part_4.png, score: 4374.999550521374
124. huub cornelius henselmans links_part_4.png, score: 4379.3970610797405
125. hannah catharina hoogendoorn links_part_4.png, score: 4379.921151161194
126. huub cornelius henselmans links_part_5.png, score: 4421.3594489097595
127. hannah catharina hoogendoorn links_part_3.png, score: 4468.936515688896
128. hannah catharina hoogendoorn rechts_part_4.png, score: 4490.3917817771435
129. egbert adrianus sanders links_part_5.png, score: 4539.394752800465
130. hannah catharina hoogendoorn rechts_part_5.png, score: 4545.016557097435
"""

list5 = """
1. lars sanders links_part_1.png, score: 1392.0234607309103
2. rene gerardus nicolaas claasens links_part_1.png, score: 1406.8056401759386
3. merel elisabeth schooneveld links_part_1.png, score: 1414.5479827821255
4. roger de jager links_part_1.png, score: 1422.0579273998737
5. merel elisabeth schooneveld rechts_part_1.png, score: 1425.395263299346
6. jolien marit sanders van opdam links_part_1.png, score: 1430.3823904842138
7. jolien marit sanders van opdam rechts_part_1.png, score: 1434.2714481651783
8. katie anne schipper rechts_part_1.png, score: 1439.2321085184813
9. lars sanders links_part_2.png, score: 1447.2406188249588
10. tobar yoska rechts_part_1.png, score: 1461.9671781361103
11. maria johanna helder links_part_1.png, score: 1467.7558222562075
12. jolien marit sanders van opdam links_part_3.png, score: 1480.3146423995495
13. katie anne schipper rechts_part_2.png, score: 1481.1173073202372
14. tobar yoska links_part_1.png, score: 1481.4780482798815
15. rene gerardus nicolaas claasens rechts_part_1.png, score: 1481.6170414239168
16. merel elisabeth schooneveld rechts_part_3.png, score: 1487.8221153616905
17. lars sanders rechts_part_2.png, score: 1488.0841142982244
18. tobar yoska links_part_2.png, score: 1489.1080140471458
19. lars sanders rechts_part_1.png, score: 1491.4012739807367
20. jolien marit sanders van opdam rechts_part_4.png, score: 1491.9478364437819
21. katie anne schipper links_part_1.png, score: 1493.2448939979076
22. jolien marit sanders van opdam links_part_2.png, score: 1493.413294017315
23. rene gerardus nicolaas claasens rechts_part_2.png, score: 1493.4988224059343
24. roger de jager rechts_part_1.png, score: 1496.7065281271935
25. maria johanna helder links_part_2.png, score: 1498.6714700311422
26. jolien marit sanders van opdam rechts_part_3.png, score: 1500.114465340972
27. merel elisabeth schooneveld rechts_part_2.png, score: 1500.8531341701746
28. katie anne schipper links_part_2.png, score: 1501.3940261900425
29. tobar yoska rechts_part_5.png, score: 1502.6089397519827
30. lars sanders rechts_part_4.png, score: 1503.0627287477255
31. egbert adrianus sanders rechts_part_1.png, score: 1512.1087661087513
32. robert vink rechts_part_1.png, score: 1512.1094114333391
33. merel elisabeth schooneveld links_part_2.png, score: 1518.0869180858135
34. tobar yoska rechts_part_2.png, score: 1521.167017802596
35. tobar yoska rechts_part_3.png, score: 1521.827669173479
36. jolien marit sanders van opdam rechts_part_2.png, score: 1523.4494325220585
37. roger de jager links_part_3.png, score: 1524.2487111985683
38. maria johanna helder rechts_part_2.png, score: 1532.7145955115557
39. robert vink links_part_1.png, score: 1535.7401742339134
40. lars sanders links_part_3.png, score: 1538.7588637918234
41. rene gerardus nicolaas claasens links_part_2.png, score: 1540.5418912023306
42. maria johanna helder links_part_3.png, score: 1544.5265390872955
43. egbert adrianus sanders links_part_1.png, score: 1545.4776877909899
44. merel elisabeth schooneveld links_part_3.png, score: 1545.581945747137
45. maria johanna helder rechts_part_3.png, score: 1550.8497427254915
46. jolien marit sanders van opdam links_part_4.png, score: 1552.8247380107641
47. huub cornelius henselmans rechts_part_3.png, score: 1558.513885051012
48. robert vink rechts_part_2.png, score: 1560.780322983861
49. maria johanna helder rechts_part_1.png, score: 1566.8141850531101
50. rachel janssen rechts_part_1.png, score: 1568.5413143187761
51. rachel janssen rechts_part_3.png, score: 1570.174837693572
52. rene gerardus nicolaas claasens links_part_3.png, score: 1571.242397710681
53. lars sanders rechts_part_3.png, score: 1572.333944156766
54. merel elisabeth schooneveld rechts_part_4.png, score: 1573.4216115623713
55. roger de jager rechts_part_2.png, score: 1573.589823514223
56. jolien marit sanders van opdam rechts_part_5.png, score: 1574.9760059267282
57. lars sanders links_part_4.png, score: 1578.5525232851505
58. rene gerardus nicolaas claasens rechts_part_3.png, score: 1580.2912082225084
59. huub cornelius henselmans rechts_part_1.png, score: 1580.9589871764183
60. roger de jager links_part_2.png, score: 1582.3985054045916
61. egbert adrianus sanders rechts_part_2.png, score: 1583.134037360549
62. merel elisabeth schooneveld links_part_4.png, score: 1587.553963035345
63. katie anne schipper links_part_3.png, score: 1594.9900889843702
64. maria johanna helder rechts_part_4.png, score: 1600.4558622986078
65. robert vink links_part_4.png, score: 1601.2781696021557
66. robert vink rechts_part_3.png, score: 1603.7105684429407
67. rachel janssen links_part_1.png, score: 1603.7846673876047
68. egbert adrianus sanders rechts_part_3.png, score: 1604.6536746621132
69. huub cornelius henselmans links_part_1.png, score: 1605.9429796785116
70. hannah catharina hoogendoorn rechts_part_2.png, score: 1607.220822274685
71. robert vink links_part_2.png, score: 1607.8876022845507
72. roger de jager links_part_4.png, score: 1610.3086962252855
73. tobar yoska links_part_5.png, score: 1617.4802450537682
74. robert vink rechts_part_4.png, score: 1620.6335118114948
75. rachel janssen links_part_2.png, score: 1621.682593896985
76. rachel janssen links_part_3.png, score: 1622.445958018303
77. rene gerardus nicolaas claasens links_part_4.png, score: 1622.5860383361578
78. rachel janssen rechts_part_2.png, score: 1627.4420646131039
79. jolien marit sanders van opdam links_part_5.png, score: 1636.5557315796614
80. tobar yoska links_part_3.png, score: 1637.2070235013962
81. tobar yoska links_part_4.png, score: 1639.8484796732664
82. merel elisabeth schooneveld links_part_5.png, score: 1654.7477628588676
83. egbert adrianus sanders links_part_2.png, score: 1657.2824831604958
84. katie anne schipper rechts_part_4.png, score: 1663.4249436706305
85. roger de jager rechts_part_4.png, score: 1666.705574825406
86. katie anne schipper links_part_5.png, score: 1667.8920897096395
87. katie anne schipper links_part_4.png, score: 1670.2792546153069
88. egbert adrianus sanders rechts_part_4.png, score: 1671.2293978184462
89. katie anne schipper rechts_part_3.png, score: 1680.7331346273422
90. robert vink rechts_part_5.png, score: 1684.376740962267
91. huub cornelius henselmans rechts_part_2.png, score: 1685.207392141223
92. merel elisabeth schooneveld rechts_part_5.png, score: 1685.2425970733166
93. roger de jager links_part_5.png, score: 1687.2501978874207
94. maria johanna helder links_part_4.png, score: 1687.8863575458527
95. robert vink links_part_3.png, score: 1688.178115427494
96. maria johanna helder rechts_part_5.png, score: 1694.4902969002724
97. egbert adrianus sanders links_part_3.png, score: 1698.028821349144
98. roger de jager rechts_part_3.png, score: 1700.6775914728642
99. hannah catharina hoogendoorn rechts_part_3.png, score: 1720.4813055545092
100. rene gerardus nicolaas claasens links_part_5.png, score: 1730.3658208251
101. robert vink links_part_5.png, score: 1732.7604867815971
102. hannah catharina hoogendoorn rechts_part_1.png, score: 1733.2182582467794
103. lars sanders links_part_5.png, score: 1738.0587974786758
104. katie anne schipper rechts_part_5.png, score: 1740.3921776115894
105. huub cornelius henselmans links_part_2.png, score: 1744.0184458494186
106. lars sanders rechts_part_5.png, score: 1744.768399566412
107. maria johanna helder links_part_5.png, score: 1792.6598425805569
108. huub cornelius henselmans rechts_part_5.png, score: 1795.5018059015274
109. huub cornelius henselmans links_part_3.png, score: 1799.2357214093208
110. rene gerardus nicolaas claasens rechts_part_4.png, score: 1803.585972636938
111. hannah catharina hoogendoorn links_part_2.png, score: 1814.205573052168
112. rachel janssen rechts_part_5.png, score: 1814.614964544773
113. huub cornelius henselmans rechts_part_4.png, score: 1825.207617789507
114. rachel janssen links_part_5.png, score: 1845.1129940450191
115. rachel janssen links_part_4.png, score: 1851.2749040722847
116. tobar yoska rechts_part_4.png, score: 1857.905785009265
117. roger de jager rechts_part_5.png, score: 1885.281565785408
118. rene gerardus nicolaas claasens rechts_part_5.png, score: 1911.9615871310234
119. huub cornelius henselmans links_part_4.png, score: 1921.822061598301
120. hannah catharina hoogendoorn links_part_5.png, score: 1937.6733997166157
121. huub cornelius henselmans links_part_5.png, score: 1950.8130259215832
122. egbert adrianus sanders rechts_part_5.png, score: 1954.2045412957668
123. hannah catharina hoogendoorn links_part_1.png, score: 1975.283977419138
124. egbert adrianus sanders links_part_4.png, score: 1984.8978413641453
125. hannah catharina hoogendoorn links_part_4.png, score: 1998.2240880429745
126. rachel janssen rechts_part_4.png, score: 2028.3263953626156
127. hannah catharina hoogendoorn links_part_3.png, score: 2082.026036530733
128. hannah catharina hoogendoorn rechts_part_4.png, score: 2114.5554782152176
129. egbert adrianus sanders links_part_5.png, score: 2130.0372949540615
130. hannah catharina hoogendoorn rechts_part_5.png, score: 2165.838317781687
"""

list6 = """
1. lars sanders links_part_1.png, score: 1380.0220625698566
2. rene gerardus nicolaas claasens links_part_1.png, score: 1406.5423076599836
3. jolien marit sanders van opdam rechts_part_1.png, score: 1408.0854529887438
4. roger de jager links_part_1.png, score: 1416.131600126624
5. merel elisabeth schooneveld rechts_part_1.png, score: 1416.579999551177
6. merel elisabeth schooneveld links_part_1.png, score: 1419.5871631205082
7. jolien marit sanders van opdam links_part_1.png, score: 1420.8708535581827
8. katie anne schipper rechts_part_1.png, score: 1422.3680177628994
9. katie anne schipper rechts_part_2.png, score: 1458.084887996316
10. lars sanders links_part_2.png, score: 1462.1828647106886
11. tobar yoska rechts_part_5.png, score: 1462.6399605572224
12. tobar yoska rechts_part_1.png, score: 1466.2187545597553
13. maria johanna helder links_part_1.png, score: 1478.616806074977
14. merel elisabeth schooneveld rechts_part_3.png, score: 1479.5326806008816
15. tobar yoska links_part_1.png, score: 1484.820634022355
16. katie anne schipper links_part_2.png, score: 1486.354612454772
17. rene gerardus nicolaas claasens rechts_part_1.png, score: 1488.9323022663593
18. jolien marit sanders van opdam links_part_2.png, score: 1490.1524212360382
19. jolien marit sanders van opdam links_part_3.png, score: 1491.8906281292439
20. katie anne schipper links_part_1.png, score: 1495.7144918739796
21. jolien marit sanders van opdam rechts_part_3.png, score: 1496.5801882743835
22. lars sanders rechts_part_2.png, score: 1500.058673247695
23. jolien marit sanders van opdam rechts_part_4.png, score: 1501.5964873731136
24. robert vink rechts_part_1.png, score: 1502.1275548189878
25. merel elisabeth schooneveld rechts_part_2.png, score: 1502.6429239660501
26. rene gerardus nicolaas claasens rechts_part_2.png, score: 1507.1448335498571
27. tobar yoska links_part_2.png, score: 1507.9735821783543
28. lars sanders rechts_part_1.png, score: 1509.940030992031
29. jolien marit sanders van opdam rechts_part_2.png, score: 1510.3648690283298
30. egbert adrianus sanders rechts_part_1.png, score: 1510.4678963422775
31. maria johanna helder links_part_2.png, score: 1512.2623276263475
32. tobar yoska rechts_part_3.png, score: 1516.0443975180387
33. roger de jager links_part_3.png, score: 1517.8526413589716
34. roger de jager rechts_part_1.png, score: 1520.5714606642723
35. merel elisabeth schooneveld links_part_2.png, score: 1523.5764163732529
36. lars sanders rechts_part_4.png, score: 1528.855365946889
37. robert vink links_part_1.png, score: 1542.0846453160048
38. lars sanders links_part_3.png, score: 1543.3713037669659
39. robert vink rechts_part_2.png, score: 1544.2132981419563
40. maria johanna helder rechts_part_2.png, score: 1550.4985843896866
41. egbert adrianus sanders links_part_1.png, score: 1554.6931890696287
42. huub cornelius henselmans rechts_part_3.png, score: 1557.5577554702759
43. rene gerardus nicolaas claasens links_part_2.png, score: 1562.7356873303652
44. tobar yoska rechts_part_2.png, score: 1566.6092144846916
45. maria johanna helder links_part_3.png, score: 1569.319987475872
46. merel elisabeth schooneveld links_part_3.png, score: 1577.2174465954304
47. maria johanna helder rechts_part_3.png, score: 1585.945695862174
48. jolien marit sanders van opdam links_part_4.png, score: 1589.3236870318651
49. rachel janssen rechts_part_3.png, score: 1591.2959371060133
50. egbert adrianus sanders rechts_part_2.png, score: 1592.7953609973192
51. roger de jager rechts_part_2.png, score: 1595.2381353527308
52. merel elisabeth schooneveld rechts_part_4.png, score: 1597.3245138078928
53. roger de jager links_part_2.png, score: 1600.791662812233
54. robert vink rechts_part_3.png, score: 1604.7240152955055
55. rachel janssen rechts_part_1.png, score: 1606.388677045703
56. jolien marit sanders van opdam rechts_part_5.png, score: 1607.9249530881643
57. lars sanders links_part_4.png, score: 1608.7991711497307
58. rene gerardus nicolaas claasens links_part_3.png, score: 1611.1722157001495
59. huub cornelius henselmans rechts_part_1.png, score: 1613.8528771698475
60. robert vink links_part_2.png, score: 1615.9379483163357
61. maria johanna helder rechts_part_1.png, score: 1618.1413582265377
62. lars sanders rechts_part_3.png, score: 1618.4137376993895
63. merel elisabeth schooneveld links_part_4.png, score: 1632.3849128186703
64. rene gerardus nicolaas claasens rechts_part_3.png, score: 1633.5968758165836
65. robert vink rechts_part_4.png, score: 1634.3458831906319
66. robert vink links_part_4.png, score: 1640.0977547317743
67. hannah catharina hoogendoorn rechts_part_2.png, score: 1640.841696113348
68. roger de jager links_part_4.png, score: 1641.842516452074
69. katie anne schipper links_part_3.png, score: 1642.355839625001
70. maria johanna helder rechts_part_4.png, score: 1644.4614395797253
71. huub cornelius henselmans links_part_1.png, score: 1647.1863837689161
72. egbert adrianus sanders rechts_part_3.png, score: 1657.53460945189
73. rachel janssen links_part_1.png, score: 1658.3876596540213
74. rachel janssen links_part_3.png, score: 1665.594107195735
75. tobar yoska links_part_5.png, score: 1666.8725540786982
76. rachel janssen rechts_part_2.png, score: 1667.2444491386414
77. rachel janssen links_part_2.png, score: 1674.350785434246
78. rene gerardus nicolaas claasens links_part_4.png, score: 1676.9334842860699
79. tobar yoska links_part_4.png, score: 1693.6516256779432
80. egbert adrianus sanders links_part_2.png, score: 1694.8252680897713
81. katie anne schipper rechts_part_4.png, score: 1695.649416089058
82. tobar yoska links_part_3.png, score: 1698.0599192529917
83. jolien marit sanders van opdam links_part_5.png, score: 1700.9775156229734
84. roger de jager rechts_part_4.png, score: 1705.0467957556248
85. egbert adrianus sanders rechts_part_4.png, score: 1713.520430535078
86. robert vink rechts_part_5.png, score: 1724.6502739787102
87. merel elisabeth schooneveld links_part_5.png, score: 1727.586744979024
88. robert vink links_part_3.png, score: 1739.8472755253315
89. katie anne schipper links_part_5.png, score: 1741.2077316343784
90. merel elisabeth schooneveld rechts_part_5.png, score: 1746.6604720652103
91. katie anne schipper links_part_4.png, score: 1747.2996361851692
92. huub cornelius henselmans rechts_part_2.png, score: 1752.1181121766567
93. katie anne schipper rechts_part_3.png, score: 1756.9234439730644
94. maria johanna helder links_part_4.png, score: 1757.5565010011196
95. maria johanna helder rechts_part_5.png, score: 1763.8101754635572
96. roger de jager links_part_5.png, score: 1768.6252128481865
97. egbert adrianus sanders links_part_3.png, score: 1773.8763609826565
98. roger de jager rechts_part_3.png, score: 1774.6751039624214
99. hannah catharina hoogendoorn rechts_part_3.png, score: 1776.6792213469744
100. robert vink links_part_5.png, score: 1801.9082018733025
101. rene gerardus nicolaas claasens links_part_5.png, score: 1812.8589274436235
102. hannah catharina hoogendoorn rechts_part_1.png, score: 1815.9779532700777
103. katie anne schipper rechts_part_5.png, score: 1816.6840933561325
104. huub cornelius henselmans links_part_2.png, score: 1818.6841120123863
105. lars sanders links_part_5.png, score: 1823.5198300778866
106. lars sanders rechts_part_5.png, score: 1843.0112080276012
107. huub cornelius henselmans rechts_part_5.png, score: 1880.4794961512089
108. rachel janssen rechts_part_5.png, score: 1899.6885401308537
109. hannah catharina hoogendoorn links_part_2.png, score: 1904.938936561346
110. huub cornelius henselmans links_part_3.png, score: 1907.6838014423847
111. maria johanna helder links_part_5.png, score: 1910.4239265322685
112. rene gerardus nicolaas claasens rechts_part_4.png, score: 1913.8348669409752
113. huub cornelius henselmans rechts_part_4.png, score: 1930.7461844086647
114. tobar yoska rechts_part_4.png, score: 1962.7791340202093
115. rachel janssen links_part_4.png, score: 1964.3711391985416
116. rachel janssen links_part_5.png, score: 1988.716504484415
117. roger de jager rechts_part_5.png, score: 2021.6630684137344
118. huub cornelius henselmans links_part_4.png, score: 2050.620465308428
119. huub cornelius henselmans links_part_5.png, score: 2052.4094318449497
120. rene gerardus nicolaas claasens rechts_part_5.png, score: 2062.7972338348627
121. hannah catharina hoogendoorn links_part_5.png, score: 2097.0222955346107
122. egbert adrianus sanders rechts_part_5.png, score: 2116.0566816329956
123. hannah catharina hoogendoorn links_part_1.png, score: 2117.696516573429
124. egbert adrianus sanders links_part_4.png, score: 2154.1701530218124
125. hannah catharina hoogendoorn links_part_4.png, score: 2158.325968950987
126. rachel janssen rechts_part_4.png, score: 2220.501892775297
127. hannah catharina hoogendoorn links_part_3.png, score: 2284.860310524702
128. hannah catharina hoogendoorn rechts_part_4.png, score: 2296.218733072281
129. egbert adrianus sanders links_part_5.png, score: 2339.2909238040447
130. hannah catharina hoogendoorn rechts_part_5.png, score: 2354.1648070812225
"""

list7 = """
1. rene gerardus nicolaas claasens links_part_1.png, score: 1270.3911292552948
2. merel elisabeth schooneveld links_part_1.png, score: 1282.4289575964212
3. roger de jager links_part_1.png, score: 1282.8258323222399
4. lars sanders links_part_1.png, score: 1285.3851133584976
5. merel elisabeth schooneveld rechts_part_1.png, score: 1293.9455493092537
6. katie anne schipper rechts_part_1.png, score: 1303.3712791651487
7. jolien marit sanders van opdam rechts_part_1.png, score: 1305.1739872545004
8. lars sanders links_part_2.png, score: 1305.5265458524227
9. jolien marit sanders van opdam links_part_1.png, score: 1308.4606665819883
10. tobar yoska rechts_part_1.png, score: 1313.0903287678957
11. rene gerardus nicolaas claasens rechts_part_1.png, score: 1319.2961675077677
12. maria johanna helder links_part_1.png, score: 1321.3558166623116
13. tobar yoska links_part_1.png, score: 1327.2425731271505
14. roger de jager rechts_part_1.png, score: 1327.3342755138874
15. lars sanders rechts_part_2.png, score: 1329.542027682066
16. rene gerardus nicolaas claasens rechts_part_2.png, score: 1337.9449249505997
17. lars sanders rechts_part_1.png, score: 1344.059863165021
18. jolien marit sanders van opdam links_part_3.png, score: 1346.7002893835306
19. maria johanna helder links_part_2.png, score: 1351.1379292309284
20. katie anne schipper links_part_1.png, score: 1353.0594059228897
21. katie anne schipper rechts_part_2.png, score: 1353.783308327198
22. jolien marit sanders van opdam links_part_2.png, score: 1353.7987800687551
23. lars sanders rechts_part_4.png, score: 1354.472737133503
24. tobar yoska links_part_2.png, score: 1360.4503251165152
25. jolien marit sanders van opdam rechts_part_4.png, score: 1361.6757770329714
26. merel elisabeth schooneveld rechts_part_3.png, score: 1362.2113108932972
27. egbert adrianus sanders rechts_part_1.png, score: 1365.0735419094563
28. tobar yoska rechts_part_2.png, score: 1367.063791051507
29. katie anne schipper links_part_2.png, score: 1367.7200181782246
30. robert vink rechts_part_1.png, score: 1373.617729216814
31. rene gerardus nicolaas claasens links_part_2.png, score: 1375.0427174121141
32. merel elisabeth schooneveld rechts_part_2.png, score: 1375.3212033510208
33. tobar yoska rechts_part_5.png, score: 1375.8046173602343
34. jolien marit sanders van opdam rechts_part_3.png, score: 1378.0722724497318
35. tobar yoska rechts_part_3.png, score: 1378.8918542265892
36. merel elisabeth schooneveld links_part_2.png, score: 1380.2404780983925
37. lars sanders links_part_3.png, score: 1383.2127235233784
38. maria johanna helder rechts_part_2.png, score: 1386.2167347669601
39. jolien marit sanders van opdam rechts_part_2.png, score: 1389.1202632337809
40. maria johanna helder links_part_3.png, score: 1391.596491008997
41. lars sanders rechts_part_3.png, score: 1394.3333533853292
42. roger de jager links_part_3.png, score: 1398.370954811573
43. maria johanna helder rechts_part_3.png, score: 1398.7059537172318
44. rene gerardus nicolaas claasens links_part_3.png, score: 1399.3375600874424
45. robert vink links_part_1.png, score: 1400.473913550377
46. merel elisabeth schooneveld links_part_3.png, score: 1403.384346112609
47. maria johanna helder rechts_part_1.png, score: 1403.6840296387672
48. egbert adrianus sanders links_part_1.png, score: 1410.2260544896126
49. rene gerardus nicolaas claasens rechts_part_3.png, score: 1413.6987352520227
50. rachel janssen rechts_part_1.png, score: 1413.8069855570793
51. jolien marit sanders van opdam links_part_4.png, score: 1417.227262854576
52. huub cornelius henselmans rechts_part_3.png, score: 1418.0868098437786
53. huub cornelius henselmans rechts_part_1.png, score: 1421.2511759847403
54. roger de jager rechts_part_2.png, score: 1423.63484659791
55. merel elisabeth schooneveld rechts_part_4.png, score: 1425.7232679277658
56. roger de jager links_part_2.png, score: 1426.539560586214
57. rachel janssen rechts_part_3.png, score: 1429.6163679510355
58. robert vink rechts_part_2.png, score: 1430.053834348917
59. merel elisabeth schooneveld links_part_4.png, score: 1431.056155219674
60. huub cornelius henselmans links_part_1.png, score: 1433.2107409536839
61. hannah catharina hoogendoorn rechts_part_2.png, score: 1436.237020432949
62. lars sanders links_part_4.png, score: 1437.648890927434
63. tobar yoska links_part_5.png, score: 1439.668913319707
64. katie anne schipper links_part_3.png, score: 1443.3603999912739
65. jolien marit sanders van opdam rechts_part_5.png, score: 1447.3131421804428
66. tobar yoska links_part_3.png, score: 1447.5554721653461
67. rachel janssen links_part_1.png, score: 1448.251901268959
68. maria johanna helder rechts_part_4.png, score: 1450.6840515136719
69. egbert adrianus sanders rechts_part_2.png, score: 1452.87260517478
70. rachel janssen links_part_2.png, score: 1454.2770032584667
71. roger de jager links_part_4.png, score: 1454.9716497957706
72. rene gerardus nicolaas claasens links_part_4.png, score: 1455.3098328262568
73. robert vink links_part_4.png, score: 1456.7262790054083
74. egbert adrianus sanders rechts_part_3.png, score: 1457.7230367809534
75. robert vink links_part_2.png, score: 1461.3349179774523
76. robert vink rechts_part_3.png, score: 1464.7477412074804
77. tobar yoska links_part_4.png, score: 1465.0632903128862
78. rachel janssen rechts_part_2.png, score: 1467.2495016157627
79. robert vink rechts_part_4.png, score: 1470.8291572630405
80. rachel janssen links_part_3.png, score: 1476.589174568653
81. jolien marit sanders van opdam links_part_5.png, score: 1479.9352362453938
82. huub cornelius henselmans rechts_part_2.png, score: 1494.3569936305285
83. merel elisabeth schooneveld links_part_5.png, score: 1501.1192274540663
84. egbert adrianus sanders rechts_part_4.png, score: 1502.5856736451387
85. egbert adrianus sanders links_part_2.png, score: 1504.590757906437
86. robert vink links_part_3.png, score: 1508.6850221902132
87. katie anne schipper rechts_part_3.png, score: 1511.5837962925434
88. roger de jager rechts_part_3.png, score: 1513.0821751654148
89. maria johanna helder links_part_4.png, score: 1513.5180774331093
90. katie anne schipper links_part_5.png, score: 1514.986635953188
91. roger de jager rechts_part_4.png, score: 1516.6488952338696
92. katie anne schipper links_part_4.png, score: 1516.6967315673828
93. katie anne schipper rechts_part_4.png, score: 1520.2643220722675
94. roger de jager links_part_5.png, score: 1529.2089984416962
95. egbert adrianus sanders links_part_3.png, score: 1530.2829161584377
96. merel elisabeth schooneveld rechts_part_5.png, score: 1531.4201141297817
97. maria johanna helder rechts_part_5.png, score: 1531.6568520516157
98. robert vink rechts_part_5.png, score: 1542.2525953501463
99. hannah catharina hoogendoorn rechts_part_3.png, score: 1549.2483974844217
100. hannah catharina hoogendoorn rechts_part_1.png, score: 1550.0467008948326
101. rene gerardus nicolaas claasens links_part_5.png, score: 1551.2121232450008
102. lars sanders rechts_part_5.png, score: 1552.6817650794983
103. robert vink links_part_5.png, score: 1555.6298532485962
104. katie anne schipper rechts_part_5.png, score: 1562.654785811901
105. lars sanders links_part_5.png, score: 1562.7087289392948
106. huub cornelius henselmans links_part_2.png, score: 1563.8073767125607
107. maria johanna helder links_part_5.png, score: 1593.393621608615
108. huub cornelius henselmans links_part_3.png, score: 1603.915348827839
109. rene gerardus nicolaas claasens rechts_part_4.png, score: 1610.3786227405071
110. huub cornelius henselmans rechts_part_5.png, score: 1613.939168855548
111. hannah catharina hoogendoorn links_part_2.png, score: 1619.1940155029297
112. huub cornelius henselmans rechts_part_4.png, score: 1629.2338750064373
113. rachel janssen rechts_part_5.png, score: 1639.830923140049
114. rachel janssen links_part_5.png, score: 1640.4846824109554
115. tobar yoska rechts_part_4.png, score: 1652.4340941607952
116. rachel janssen links_part_4.png, score: 1669.447536945343
117. roger de jager rechts_part_5.png, score: 1675.2988033890724
118. rene gerardus nicolaas claasens rechts_part_5.png, score: 1703.3558714985847
119. hannah catharina hoogendoorn links_part_5.png, score: 1716.41473954916
120. huub cornelius henselmans links_part_4.png, score: 1717.9242654144764
121. egbert adrianus sanders rechts_part_5.png, score: 1738.0908392071724
122. egbert adrianus sanders links_part_4.png, score: 1750.0622972846031
123. hannah catharina hoogendoorn links_part_1.png, score: 1751.1040544211864
124. hannah catharina hoogendoorn links_part_4.png, score: 1763.285017579794
125. huub cornelius henselmans links_part_5.png, score: 1769.1671425402164
126. rachel janssen rechts_part_4.png, score: 1803.1115937829018
127. hannah catharina hoogendoorn links_part_3.png, score: 1846.8246522843838
128. hannah catharina hoogendoorn rechts_part_4.png, score: 1865.1276614069939
129. egbert adrianus sanders links_part_5.png, score: 1898.6837442219257
130. hannah catharina hoogendoorn rechts_part_5.png, score: 1924.6314715147018
"""


# Aggregate scores from the two lists
aggregated_scores = aggregate_scores(list2)

# Print the scores, with each name on a new line
print_scores(aggregated_scores)