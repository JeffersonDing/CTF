(module
  (table $table0 1 1 funcref)
  (memory $memory (;0;) (export "memory") 2)
  (global $global0 (mut i32) (i32.const 66864))
  (global $input (;1;) (export "input") i32 (i32.const 1072))
  (global $__dso_handle (;2;) (export "__dso_handle") i32 (i32.const 1024))
  (global $__data_end (;3;) (export "__data_end") i32 (i32.const 1328))
  (global $__global_base (;4;) (export "__global_base") i32 (i32.const 1024))
  (global $__heap_base (;5;) (export "__heap_base") i32 (i32.const 66864))
  (global $__memory_base (;6;) (export "__memory_base") i32 (i32.const 0))
  (global $__table_base (;7;) (export "__table_base") i32 (i32.const 1))
  (func $__wasm_call_ctors (;0;) (export "__wasm_call_ctors")
  )
  (func $strcmp (;1;) (export "strcmp") (param $var0 i32) (param $var1 i32) (result i32)
    (local $var2 i32) (local $var3 i32) (local $var4 i32) (local $var5 i32) (local $var6 i32) (local $var7 i32) (local $var8 i32) (local $var9 i32) (local $var10 i32) (local $var11 i32) (local $var12 i32) (local $var13 i32) (local $var14 i32) (local $var15 i32) (local $var16 i32) (local $var17 i32) (local $var18 i32) (local $var19 i32) (local $var20 i32) (local $var21 i32) (local $var22 i32) (local $var23 i32) (local $var24 i32) (local $var25 i32) (local $var26 i32) (local $var27 i32) (local $var28 i32) (local $var29 i32) (local $var30 i32) (local $var31 i32) (local $var32 i32) (local $var33 i32) (local $var34 i32) (local $var35 i32) (local $var36 i32) (local $var37 i32) (local $var38 i32) (local $var39 i32) (local $var40 i32) (local $var41 i32) (local $var42 i32) (local $var43 i32)
    global.get $global0
    local.set $var2
    i32.const 32
    local.set $var3
    local.get $var2
    local.get $var3
    i32.sub
    local.set $var4
    local.get $var4
    local.get $var0
    i32.store offset=24
    local.get $var4
    local.get $var1
    i32.store offset=20
    local.get $var4
    i32.load offset=24
    local.set $var5
    local.get $var4
    local.get $var5
    i32.store offset=16
    local.get $var4
    i32.load offset=20
    local.set $var6
    local.get $var4
    local.get $var6
    i32.store offset=12
    block $label1
      loop $label2
        local.get $var4
        i32.load offset=16
        local.set $var7
        i32.const 1
        local.set $var8
        local.get $var7
        local.get $var8
        i32.add
        local.set $var9
        local.get $var4
        local.get $var9
        i32.store offset=16
        local.get $var7
        i32.load8_u
        local.set $var10
        local.get $var4
        local.get $var10
        i32.store8 offset=11
        local.get $var4
        i32.load offset=12
        local.set $var11
        i32.const 1
        local.set $var12
        local.get $var11
        local.get $var12
        i32.add
        local.set $var13
        local.get $var4
        local.get $var13
        i32.store offset=12
        local.get $var11
        i32.load8_u
        local.set $var14
        local.get $var4
        local.get $var14
        i32.store8 offset=10
        local.get $var4
        i32.load8_u offset=11
        local.set $var15
        i32.const 255
        local.set $var16
        local.get $var15
        local.get $var16
        i32.and
        local.set $var17
        block $label0
          local.get $var17
          br_if $label0
          local.get $var4
          i32.load8_u offset=11
          local.set $var18
          i32.const 255
          local.set $var19
          local.get $var18
          local.get $var19
          i32.and
          local.set $var20
          local.get $var4
          i32.load8_u offset=10
          local.set $var21
          i32.const 255
          local.set $var22
          local.get $var21
          local.get $var22
          i32.and
          local.set $var23
          local.get $var20
          local.get $var23
          i32.sub
          local.set $var24
          local.get $var4
          local.get $var24
          i32.store offset=28
          br $label1
        end $label0
        local.get $var4
        i32.load8_u offset=11
        local.set $var25
        i32.const 255
        local.set $var26
        local.get $var25
        local.get $var26
        i32.and
        local.set $var27
        local.get $var4
        i32.load8_u offset=10
        local.set $var28
        i32.const 255
        local.set $var29
        local.get $var28
        local.get $var29
        i32.and
        local.set $var30
        local.get $var27
        local.set $var31
        local.get $var30
        local.set $var32
        local.get $var31
        local.get $var32
        i32.eq
        local.set $var33
        i32.const 1
        local.set $var34
        local.get $var33
        local.get $var34
        i32.and
        local.set $var35
        local.get $var35
        br_if $label2
      end $label2
      local.get $var4
      i32.load8_u offset=11
      local.set $var36
      i32.const 255
      local.set $var37
      local.get $var36
      local.get $var37
      i32.and
      local.set $var38
      local.get $var4
      i32.load8_u offset=10
      local.set $var39
      i32.const 255
      local.set $var40
      local.get $var39
      local.get $var40
      i32.and
      local.set $var41
      local.get $var38
      local.get $var41
      i32.sub
      local.set $var42
      local.get $var4
      local.get $var42
      i32.store offset=28
    end $label1
    local.get $var4
    i32.load offset=28
    local.set $var43
    local.get $var43
    return
  )
  (func $check_flag (;2;) (export "check_flag") (result i32)
    (local $var0 i32) (local $var1 i32) (local $var2 i32) (local $var3 i32) (local $var4 i32) (local $var5 i32) (local $var6 i32) (local $var7 i32) (local $var8 i32) (local $var9 i32) (local $var10 i32) (local $var11 i32) (local $var12 i32) (local $var13 i32) (local $var14 i32) (local $var15 i32) (local $var16 i32) (local $var17 i32) (local $var18 i32) (local $var19 i32) (local $var20 i32) (local $var21 i32) (local $var22 i32) (local $var23 i32) (local $var24 i32) (local $var25 i32) (local $var26 i32) (local $var27 i32) (local $var28 i32) (local $var29 i32) (local $var30 i32) (local $var31 i32) (local $var32 i32) (local $var33 i32) (local $var34 i32) (local $var35 i32) (local $var36 i32) (local $var37 i32) (local $var38 i32) (local $var39 i32) (local $var40 i32) (local $var41 i32) (local $var42 i32) (local $var43 i32) (local $var44 i32) (local $var45 i32) (local $var46 i32) (local $var47 i32) (local $var48 i32) (local $var49 i32) (local $var50 i32) (local $var51 i32) (local $var52 i32) (local $var53 i32) (local $var54 i32) (local $var55 i32) (local $var56 i32) (local $var57 i32) (local $var58 i32) (local $var59 i32) (local $var60 i32) (local $var61 i32) (local $var62 i32) (local $var63 i32) (local $var64 i32) (local $var65 i32) (local $var66 i32) (local $var67 i32) (local $var68 i32) (local $var69 i32) (local $var70 i32) (local $var71 i32) (local $var72 i32) (local $var73 i32) (local $var74 i32) (local $var75 i32) (local $var76 i32) (local $var77 i32) (local $var78 i32) (local $var79 i32) (local $var80 i32) (local $var81 i32) (local $var82 i32) (local $var83 i32) (local $var84 i32) (local $var85 i32) (local $var86 i32) (local $var87 i32) (local $var88 i32) (local $var89 i32) (local $var90 i32) (local $var91 i32) (local $var92 i32) (local $var93 i32) (local $var94 i32) (local $var95 i32) (local $var96 i32) (local $var97 i32) (local $var98 i32) (local $var99 i32) (local $var100 i32) (local $var101 i32) (local $var102 i32) (local $var103 i32) (local $var104 i32) (local $var105 i32) (local $var106 i32) (local $var107 i32) (local $var108 i32) (local $var109 i32) (local $var110 i32) (local $var111 i32) (local $var112 i32) (local $var113 i32) (local $var114 i32) (local $var115 i32) (local $var116 i32) (local $var117 i32) (local $var118 i32) (local $var119 i32) (local $var120 i32) (local $var121 i32) (local $var122 i32) (local $var123 i32) (local $var124 i32) (local $var125 i32) (local $var126 i32) (local $var127 i32) (local $var128 i32) (local $var129 i32) (local $var130 i32) (local $var131 i32) (local $var132 i32) (local $var133 i32) (local $var134 i32) (local $var135 i32) (local $var136 i32) (local $var137 i32) (local $var138 i32) (local $var139 i32) (local $var140 i32) (local $var141 i32) (local $var142 i32) (local $var143 i32) (local $var144 i32) (local $var145 i32) (local $var146 i32) (local $var147 i32) (local $var148 i32) (local $var149 i32) (local $var150 i32) (local $var151 i32) (local $var152 i32) (local $var153 i32) (local $var154 i32) (local $var155 i32) (local $var156 i32) (local $var157 i32) (local $var158 i32) (local $var159 i32) (local $var160 i32) (local $var161 i32) (local $var162 i32) (local $var163 i32) (local $var164 i32)
    global.get $global0
    local.set $var0
    i32.const 16
    local.set $var1
    local.get $var0
    local.get $var1
    i32.sub
    local.set $var2
    local.get $var2
    global.set $global0
    i32.const 0
    local.set $var3
    local.get $var2
    local.get $var3
    i32.store offset=12
    block $label0
      loop $label9
        local.get $var2
        i32.load offset=12
        local.set $var4
        local.get $var4
        i32.load8_u offset=1072
        local.set $var5
        i32.const 24
        local.set $var6
        local.get $var5
        local.get $var6
        i32.shl
        local.set $var7
        local.get $var7
        local.get $var6
        i32.shr_s
        local.set $var8
        local.get $var8
        i32.eqz
        br_if $label0
        i32.const 0
        local.set $var9
        local.get $var2
        i32.load offset=12
        local.set $var10
        local.get $var10
        i32.load8_u offset=1072
        local.set $var11
        i32.const 24
        local.set $var12
        local.get $var11
        local.get $var12
        i32.shl
        local.set $var13
        local.get $var13
        local.get $var12
        i32.shr_s
        local.set $var14
        i32.const 20
        local.set $var15
        local.get $var14
        local.get $var15
        i32.xor
        local.set $var16
        local.get $var10
        local.get $var16
        i32.store8 offset=1072
        local.get $var2
        i32.load offset=12
        local.set $var17
        local.get $var17
        local.set $var18
        local.get $var9
        local.set $var19
        local.get $var18
        local.get $var19
        i32.gt_s
        local.set $var20
        i32.const 1
        local.set $var21
        local.get $var20
        local.get $var21
        i32.and
        local.set $var22
        block $label1
          local.get $var22
          i32.eqz
          br_if $label1
          local.get $var2
          i32.load offset=12
          local.set $var23
          i32.const 1
          local.set $var24
          local.get $var23
          local.get $var24
          i32.sub
          local.set $var25
          local.get $var25
          i32.load8_u offset=1072
          local.set $var26
          i32.const 24
          local.set $var27
          local.get $var26
          local.get $var27
          i32.shl
          local.set $var28
          local.get $var28
          local.get $var27
          i32.shr_s
          local.set $var29
          local.get $var2
          i32.load offset=12
          local.set $var30
          local.get $var30
          i32.load8_u offset=1072
          local.set $var31
          i32.const 24
          local.set $var32
          local.get $var31
          local.get $var32
          i32.shl
          local.set $var33
          local.get $var33
          local.get $var32
          i32.shr_s
          local.set $var34
          local.get $var34
          local.get $var29
          i32.xor
          local.set $var35
          local.get $var30
          local.get $var35
          i32.store8 offset=1072
        end $label1
        i32.const 2
        local.set $var36
        local.get $var2
        i32.load offset=12
        local.set $var37
        local.get $var37
        local.set $var38
        local.get $var36
        local.set $var39
        local.get $var38
        local.get $var39
        i32.gt_s
        local.set $var40
        i32.const 1
        local.set $var41
        local.get $var40
        local.get $var41
        i32.and
        local.set $var42
        block $label2
          local.get $var42
          i32.eqz
          br_if $label2
          local.get $var2
          i32.load offset=12
          local.set $var43
          i32.const 3
          local.set $var44
          local.get $var43
          local.get $var44
          i32.sub
          local.set $var45
          local.get $var45
          i32.load8_u offset=1072
          local.set $var46
          i32.const 24
          local.set $var47
          local.get $var46
          local.get $var47
          i32.shl
          local.set $var48
          local.get $var48
          local.get $var47
          i32.shr_s
          local.set $var49
          local.get $var2
          i32.load offset=12
          local.set $var50
          local.get $var50
          i32.load8_u offset=1072
          local.set $var51
          i32.const 24
          local.set $var52
          local.get $var51
          local.get $var52
          i32.shl
          local.set $var53
          local.get $var53
          local.get $var52
          i32.shr_s
          local.set $var54
          local.get $var54
          local.get $var49
          i32.xor
          local.set $var55
          local.get $var50
          local.get $var55
          i32.store8 offset=1072
        end $label2
        local.get $var2
        i32.load offset=12
        local.set $var56
        i32.const 10
        local.set $var57
        local.get $var56
        local.get $var57
        i32.rem_s
        local.set $var58
        local.get $var2
        i32.load offset=12
        local.set $var59
        local.get $var59
        i32.load8_u offset=1072
        local.set $var60
        i32.const 24
        local.set $var61
        local.get $var60
        local.get $var61
        i32.shl
        local.set $var62
        local.get $var62
        local.get $var61
        i32.shr_s
        local.set $var63
        local.get $var63
        local.get $var58
        i32.xor
        local.set $var64
        local.get $var59
        local.get $var64
        i32.store8 offset=1072
        local.get $var2
        i32.load offset=12
        local.set $var65
        i32.const 2
        local.set $var66
        local.get $var65
        local.get $var66
        i32.rem_s
        local.set $var67
        block $label4
          block $label3
            local.get $var67
            br_if $label3
            local.get $var2
            i32.load offset=12
            local.set $var68
            local.get $var68
            i32.load8_u offset=1072
            local.set $var69
            i32.const 24
            local.set $var70
            local.get $var69
            local.get $var70
            i32.shl
            local.set $var71
            local.get $var71
            local.get $var70
            i32.shr_s
            local.set $var72
            i32.const 9
            local.set $var73
            local.get $var72
            local.get $var73
            i32.xor
            local.set $var74
            local.get $var68
            local.get $var74
            i32.store8 offset=1072
            br $label4
          end $label3
          local.get $var2
          i32.load offset=12
          local.set $var75
          local.get $var75
          i32.load8_u offset=1072
          local.set $var76
          i32.const 24
          local.set $var77
          local.get $var76
          local.get $var77
          i32.shl
          local.set $var78
          local.get $var78
          local.get $var77
          i32.shr_s
          local.set $var79
          i32.const 8
          local.set $var80
          local.get $var79
          local.get $var80
          i32.xor
          local.set $var81
          local.get $var75
          local.get $var81
          i32.store8 offset=1072
        end $label4
        local.get $var2
        i32.load offset=12
        local.set $var82
        i32.const 3
        local.set $var83
        local.get $var82
        local.get $var83
        i32.rem_s
        local.set $var84
        block $label6
          block $label5
            local.get $var84
            br_if $label5
            local.get $var2
            i32.load offset=12
            local.set $var85
            local.get $var85
            i32.load8_u offset=1072
            local.set $var86
            i32.const 24
            local.set $var87
            local.get $var86
            local.get $var87
            i32.shl
            local.set $var88
            local.get $var88
            local.get $var87
            i32.shr_s
            local.set $var89
            i32.const 7
            local.set $var90
            local.get $var89
            local.get $var90
            i32.xor
            local.set $var91
            local.get $var85
            local.get $var91
            i32.store8 offset=1072
            br $label6
          end $label5
          i32.const 1
          local.set $var92
          local.get $var2
          i32.load offset=12
          local.set $var93
          i32.const 3
          local.set $var94
          local.get $var93
          local.get $var94
          i32.rem_s
          local.set $var95
          local.get $var95
          local.set $var96
          local.get $var92
          local.set $var97
          local.get $var96
          local.get $var97
          i32.eq
          local.set $var98
          i32.const 1
          local.set $var99
          local.get $var98
          local.get $var99
          i32.and
          local.set $var100
          block $label8
            block $label7
              local.get $var100
              i32.eqz
              br_if $label7
              local.get $var2
              i32.load offset=12
              local.set $var101
              local.get $var101
              i32.load8_u offset=1072
              local.set $var102
              i32.const 24
              local.set $var103
              local.get $var102
              local.get $var103
              i32.shl
              local.set $var104
              local.get $var104
              local.get $var103
              i32.shr_s
              local.set $var105
              i32.const 6
              local.set $var106
              local.get $var105
              local.get $var106
              i32.xor
              local.set $var107
              local.get $var101
              local.get $var107
              i32.store8 offset=1072
              br $label8
            end $label7
            local.get $var2
            i32.load offset=12
            local.set $var108
            local.get $var108
            i32.load8_u offset=1072
            local.set $var109
            i32.const 24
            local.set $var110
            local.get $var109
            local.get $var110
            i32.shl
            local.set $var111
            local.get $var111
            local.get $var110
            i32.shr_s
            local.set $var112
            i32.const 5
            local.set $var113
            local.get $var112
            local.get $var113
            i32.xor
            local.set $var114
            local.get $var108
            local.get $var114
            i32.store8 offset=1072
          end $label8
        end $label6
        local.get $var2
        i32.load offset=12
        local.set $var115
        i32.const 1
        local.set $var116
        local.get $var115
        local.get $var116
        i32.add
        local.set $var117
        local.get $var2
        local.get $var117
        i32.store offset=12
        br $label9
      end $label9
    end $label0
    i32.const 0
    local.set $var118
    local.get $var2
    local.get $var118
    i32.store offset=4
    block $label10
      loop $label12
        local.get $var2
        i32.load offset=4
        local.set $var119
        local.get $var2
        i32.load offset=12
        local.set $var120
        local.get $var119
        local.set $var121
        local.get $var120
        local.set $var122
        local.get $var121
        local.get $var122
        i32.lt_s
        local.set $var123
        i32.const 1
        local.set $var124
        local.get $var123
        local.get $var124
        i32.and
        local.set $var125
        local.get $var125
        i32.eqz
        br_if $label10
        local.get $var2
        i32.load offset=4
        local.set $var126
        i32.const 2
        local.set $var127
        local.get $var126
        local.get $var127
        i32.rem_s
        local.set $var128
        block $label11
          local.get $var128
          br_if $label11
          local.get $var2
          i32.load offset=4
          local.set $var129
          i32.const 1
          local.set $var130
          local.get $var129
          local.get $var130
          i32.add
          local.set $var131
          local.get $var2
          i32.load offset=12
          local.set $var132
          local.get $var131
          local.set $var133
          local.get $var132
          local.set $var134
          local.get $var133
          local.get $var134
          i32.lt_s
          local.set $var135
          i32.const 1
          local.set $var136
          local.get $var135
          local.get $var136
          i32.and
          local.set $var137
          local.get $var137
          i32.eqz
          br_if $label11
          local.get $var2
          i32.load offset=4
          local.set $var138
          local.get $var138
          i32.load8_u offset=1072
          local.set $var139
          local.get $var2
          local.get $var139
          i32.store8 offset=11
          local.get $var2
          i32.load offset=4
          local.set $var140
          i32.const 1
          local.set $var141
          local.get $var140
          local.get $var141
          i32.add
          local.set $var142
          local.get $var142
          i32.load8_u offset=1072
          local.set $var143
          local.get $var2
          i32.load offset=4
          local.set $var144
          local.get $var144
          local.get $var143
          i32.store8 offset=1072
          local.get $var2
          i32.load8_u offset=11
          local.set $var145
          local.get $var2
          i32.load offset=4
          local.set $var146
          i32.const 1
          local.set $var147
          local.get $var146
          local.get $var147
          i32.add
          local.set $var148
          local.get $var148
          local.get $var145
          i32.store8 offset=1072
        end $label11
        local.get $var2
        i32.load offset=4
        local.set $var149
        i32.const 1
        local.set $var150
        local.get $var149
        local.get $var150
        i32.add
        local.set $var151
        local.get $var2
        local.get $var151
        i32.store offset=4
        br $label12
      end $label12
    end $label10
    i32.const 0
    local.set $var152
    i32.const 1072
    local.set $var153
    i32.const 1024
    local.set $var154
    local.get $var154
    local.get $var153
    call $strcmp
    local.set $var155
    local.get $var155
    local.set $var156
    local.get $var152
    local.set $var157
    local.get $var156
    local.get $var157
    i32.ne
    local.set $var158
    i32.const -1
    local.set $var159
    local.get $var158
    local.get $var159
    i32.xor
    local.set $var160
    i32.const 1
    local.set $var161
    local.get $var160
    local.get $var161
    i32.and
    local.set $var162
    i32.const 16
    local.set $var163
    local.get $var2
    local.get $var163
    i32.add
    local.set $var164
    local.get $var164
    global.set $global0
    local.get $var162
    return
  )
  (func $copy_char (;3;) (export "copy_char") (param $var0 i32) (param $var1 i32)
    (local $var2 i32) (local $var3 i32) (local $var4 i32) (local $var5 i32) (local $var6 i32)
    global.get $global0
    local.set $var2
    i32.const 16
    local.set $var3
    local.get $var2
    local.get $var3
    i32.sub
    local.set $var4
    local.get $var4
    local.get $var0
    i32.store offset=12
    local.get $var4
    local.get $var1
    i32.store offset=8
    local.get $var4
    i32.load offset=12
    local.set $var5
    local.get $var4
    i32.load offset=8
    local.set $var6
    local.get $var6
    local.get $var5
    i32.store8 offset=1072
    return
  )
  (data (i32.const 1024) "\18j|a\118i7[H~Jh^Ko\1f]\5cw4kP\15pO?\5cEo\14\06\05}>=\04\16.\12L\00\00")
)