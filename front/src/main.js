import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from "pinia"
import VueMobileDetection from 'vue-mobile-detection'
import * as Sentry from "@sentry/vue";

// Vuetify
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'



// Sentry.init({
//     App,
//     dsn: "https://1c1f8712a989433cb34416dd0bfde82e@o4505030048284672.ingest.sentry.io/4505030053330944",
//     integrations: [
//         new Sentry.BrowserTracing({
//             routingInstrumentation: Sentry.vueRouterInstrumentation(router),
//             tracePropagationTargets: ["kmapshot.com", /^\//],
//         }),
//     ],

//     tracesSampleRate: 1,
// });

const vuetify = createVuetify({
    components,
    directives,
})

createApp(App).use(createPinia()).use(router).use(vuetify).use(VueMobileDetection).mount('#app')
