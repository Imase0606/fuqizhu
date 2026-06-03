const { test, expect } = require("@playwright/test");

test("H5 interactions work", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("file:///D:/develop/notforme/fuqizhu/index.html");
  await page.click('[data-stage="grow"]');
  await expect(page.locator("#grow")).toBeVisible();

  await page.fill("#mistakeInput", "我曾经害怕失败，所以错过了一次展示自己的机会。");
  await page.click("#fixMistake");
  await expect(page.locator("#userNote")).toContainText("我的成长错题");

  await page.fill("#name", "同岁青年");
  await page.fill("#wishText", "愿我在未来仍然保留热爱，也敢于重新开始。");
  await page.click("text=封存心愿");
  await expect(page.locator("#wishResult")).toContainText("心愿盲盒已封存");

  await page.screenshot({ path: "output/playwright/mobile-interaction.png" });
});
