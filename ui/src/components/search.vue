<template>
    <div class="search-field">
        <q-input
            dense
            outlined
            class="bg-grey-3"
            :modelValue="modelValue"
            :placeholder="placeholder"
            @update:modelValue="updateModelValue"
            color="blue"
            :debounce="500"
        >
            <template v-slot:append>
                <q-icon
                    v-if="modelValue !== ''"
                    name="close"
                    class="cursor-pointer"
                    @click="updateModelValue('')"
                    size="20px"
                />
                <q-icon name="search" size="20px"/>
            </template>
        </q-input>
    </div>
</template>
<script>
export default {
    name: 'search-field',
    props: {
        modelValue: {
            type: String,
            required: true,
            default: '',
        },
        placeholder: {
            type: String,
            default: '',
        },
    },
    methods: {
        updateModelValue(value) {
            this.$emit('update:modelValue', value);
        },
    },
};
</script>
<style lang="scss">
.search-field {
    display: flex;
    justify-content: flex-end;
    margin-top: 12px;

    .q-field {
        padding-bottom: 0;
    }
}
</style>
