<template>
    <q-input :modelValue="modelValue" mask="##/##/####" dense outlined
        :rules="[validate]"
    >
        <template v-slot:append>
            <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy
                    ref="qDateProxy"
                    cover transition-show="scale"
                    transition-hide="scale"
                >
                    <q-date
                        :modelValue="modelValue"
                        minimal mask="MM/DD/YYYY"
                        @update:modelValue="$emit('update:modelValue', $event)"
                    >
                        <div class="row items-center justify-end">
                            <q-btn v-close-popup label="Close" color="primary" flat />
                        </div>
                    </q-date>
                </q-popup-proxy>
            </q-icon>
        </template>
    </q-input>
</template>
<script>
export default {
    name: 'date-picker',
    props: {
        modelValue: {
            type: String,
            default: '',
        },
        required: {
            type: Boolean,
            default: false,
        },
    },
    emits: ['update:modelValue'],
    methods: {
        validate(date) {
            if (this.required) {
                return Boolean(date) || 'This field is required.';
            }
            return true;
        },
    },
};
</script>
