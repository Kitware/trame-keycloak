import Keycloak from "keycloak-js";
import { inject, ref, onMounted } from "vue";

function getState(keycloak) {
  const { authenticated, subject, roles, resourceAccess } = keycloak;
  return {
    authenticated,
    subject,
    roles,
    resourceAccess,
  };
}

export default {
  props: ["config"],
  emits: ["authenticated", "profile"],
  setup(props, { emit }) {
    const profile = ref(null);
    const authenticated = ref(false);
    const keycloak = new Keycloak(props.config);
    inject("keycloak", keycloak);

    function login(options) {
      return keycloak.login(options);
    }
    function logout(options) {
      return keycloak.logout(options);
    }

    function register(options) {
      return keycloak.register(options);
    }

    function hasRealmRole(role) {
      return keycloak.hasRealmRole(role);
    }

    function hasResourceRole(role, resource) {
      return keycloak.hasResourceRole(role, resource);
    }

    onMounted(() => {
      keycloak
        .init({ onLoad: props.config.onLoad, flow: props.config?.flow || "" })
        .then(async (auth) => {
          if (!auth) {
            emit("authenticated", false);
            window.location.reload();
          } else {
            emit("authenticated", getState(keycloak));
            profile.value = await keycloak.loadUserProfile();
            emit("profile", profile.value);
          }
          authenticated.value = auth;
        });
    });
    return {
      authenticated,
      login,
      logout,
      register,
      hasRealmRole,
      hasResourceRole,
    };
  },
  // v-slot="{ user }"
  template: '<slot v-if="authenticated" :user="profile"></slot>',
};
