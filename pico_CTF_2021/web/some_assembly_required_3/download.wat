(module
  (table $table0 1 1 funcref)
  (memory $memory (;0;) (export "memory") 2)
  (global $global0 (mut i32) (i32.const 66864))
  (global $input (;1;) (export "input") i32 (i32.const 1072))
  (global $key (;2;) (export "key") i32 (i32.const 1067))
  (global $__dso_handle (;3;) (export "__dso_handle") i32 (i32.const 1024))
  (global $__data_end (;4;) (export "__data_end") i32 (i32.const 1328))
  (global $__global_base (;5;) (export "__global_base") i32 (i32.const 1024))
  (global $__heap_base (;6;) (export "__heap_base") i32 (i32.const 66864))
  (global $__memory_base (;7;) (export "__memory_base") i32 (i32.const 0))
  (global $__table_base (;8;) (export "__table_base") i32 (i32.const 1))
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
    (local $var0 i32) (local $var1 i32) (local $var2 i32) (local $var3 i32) (local $var4 i32) (local $var5 i32) (local $var6 i32) (local $var7 i32) (local $var8 i32) (local $var9 i32) (local $var10 i32)
    i32.const 0
    local.set $var0
    i32.const 1072
    local.set $var1
    i32.const 1024
    local.set $var2
    local.get $var2
    local.get $var1
    call $strcmp
    local.set $var3
    local.get $var3
    local.set $var4
    local.get $var0
    local.set $var5
    local.get $var4
    local.get $var5
    i32.ne
    local.set $var6
    i32.const -1
    local.set $var7
    local.get $var6
    local.get $var7
    i32.xor
    local.set $var8
    i32.const 1
    local.set $var9
    local.get $var8
    local.get $var9
    i32.and
    local.set $var10
    local.get $var10
    return
  )
  (func $copy_char (;3;) (export "copy_char") (param $var0 i32) (param $var1 i32)
    (local $var2 i32) (local $var3 i32) (local $var4 i32) (local $var5 i32) (local $var6 i32) (local $var7 i32) (local $var8 i32) (local $var9 i32) (local $var10 i32) (local $var11 i32) (local $var12 i32) (local $var13 i32) (local $var14 i32) (local $var15 i32) (local $var16 i32) (local $var17 i32) (local $var18 i32)
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
    block $label0
      local.get $var5
      i32.eqz
      br_if $label0
      i32.const 4
      local.set $var6
      local.get $var4
      i32.load offset=8
      local.set $var7
      i32.const 5
      local.set $var8
      local.get $var7
      local.get $var8
      i32.rem_s
      local.set $var9
      local.get $var6
      local.get $var9
      i32.sub
      local.set $var10
      local.get $var10
      i32.load8_u offset=1067
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
      local.get $var4
      i32.load offset=12
      local.set $var15
      local.get $var15
      local.get $var14
      i32.xor
      local.set $var16
      local.get $var4
      local.get $var16
      i32.store offset=12
    end $label0
    local.get $var4
    i32.load offset=12
    local.set $var17
    local.get $var4
    i32.load offset=8
    local.set $var18
    local.get $var18
    local.get $var17
    i32.store8 offset=1072
    return
  )
  (data (i32.const 1024) "\9dn\93\c8\b2\b9A\8b\94\c6\df3\c0\c5\95\de7\c3\9f\93\df?\c9\c3\c2\8c2\93\90\c1\8ee\95\9f\c2\8c6\c8\95\c0\90\00\00")
  (data (i32.const 1067) "\f1\a7\f0\07\ed")
)