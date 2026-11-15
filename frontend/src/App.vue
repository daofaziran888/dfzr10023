<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">茶道修习传承管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向中华茶道修习的茶样鉴藏、茶席布置、点茶研习、茶具养护与雅集筹办的一体化传承管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "茶样鉴藏", path: "/tea_leaf" }, { label: "茶人档案", path: "/tea_master" }, { label: "门生修习", path: "/disciple" }, { label: "茶具养护", path: "/tea_set" }, { label: "茶席布置", path: "/tea_mat" }, { label: "点茶研习", path: "/dian_cha" }, { label: "用水品鉴", path: "/tea_water" }, { label: "香道搭配", path: "/tea_incense" }, { label: "茶会雅集", path: "/tea_ceremony" }, { label: "茶诗茶画", path: "/tea_poetry" }, { label: "茶书典籍", path: "/tea_book" }, { label: "茶区探访", path: "/tea_region" }, { label: "制茶工坊", path: "/tea_workshop" }, { label: "斗茶赛会", path: "/tea_contest" }, { label: "茶礼往来", path: "/tea_exchange" }, { label: "影像记录", path: "/tea_media" }, { label: "传承基金", path: "/tea_fund" }]
</script>
