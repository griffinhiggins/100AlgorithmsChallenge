def reflectString(s):
    ret_s = ''
    mid = int((ord('a') + ord('z')) / 2)
    for x in list(s):
                 #---------CASE1---------                        #----------CASE2----------
        ret_s += chr((mid+1)+(mid-ord(x))) if ord(x) <= mid else chr((mid)-(ord(x)-(mid+1)))
        """
        ============================================================
        CASE1 (src <= mid): e -> v
            1. d=mid-src
            2. dest=mid+1+d   

                    src=101           mid=109           dest=118      
            a b c d [e] f g h i j k l m n o p q r s t u [v] w x y z
                    <-----------------|------------------>   
                    d=109-101=8         dest=(109+1)+8=118
        ============================================================
        CASE2 (src > mid): v -> e
            1. d=src-mid+1
            2. dest=mid-d

                    dest=101           mid=109           src=118      
            a b c d [e] f g h i j k l m n o p q r s t u [v] w x y z
                    <-----------------|------------------>   
                    dest=109-108=101         d=118-109+1=8
        ============================================================
        """

    return ret_s
print(reflectString('name'))
print(reflectString('zyxwvutsrqpon'))
