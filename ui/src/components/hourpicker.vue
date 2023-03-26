<template>
    <q-input :modelValue="modelValue" mask="##:##" dense outlined
        :rules="[validate]"
    >
        <template v-slot:append>
            <q-icon name="mdi-calendar-clock" class="cursor-pointer">
                <q-popup-proxy
                    ref="qHourProxy"
                    cover transition-show="scale"
                    transition-hide="scale"
                >
                    <q-time
                        :modelValue="modelValue"
                        minimal mask="HH:mm"
                        @update:modelValue="$emit('update:modelValue', $event)"
                        format24h
                    >
                        <div class="row items-center justify-end">
                            <q-btn v-close-popup label="Close" color="primary" flat />
                        </div>
                    </q-time>
                </q-popup-proxy>
            </q-icon>
        </template>
    </q-input>
</template>
<script>
export default {
    name: 'hour-picker',
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
        validate(hour) {
            if (this.required) {
                return Boolean(hour) || 'This field is required.';
            }
            return true;
        },
    },
};
</script>
