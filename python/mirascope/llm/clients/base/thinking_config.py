"""Configuration for LLM thinking / reasoning."""

from typing import TypedDict


class ThinkingConfig(TypedDict, total=False):
    """Allows for configuration of model thinking behavior.

    The `ThinkingConfig` allows you to configure how much effort/tokens the model will
    put into its reasoning process before generating a response. In order to abstract
    over providers, effort is encoded as a scalar value between 0 and 1.

    If you wish to disable thinking, set `thinking=False` or use a `ThinkingConfig` with
    `effort == 0`. Note not all models allow fully disabling thinking; in such cases, we
    will instead minimize thinking.
    """

    summaries: bool
    """Whether the model should generate thinking summaries to include as `Thought`s.

    Behavior of this parameter is provider-specific. Some providers (e.g. Anthropic) always
    provide `Thinking` outputs. Others (e.g. Google, OpenAI) will do so only if requested
    via this parameter. 

    If unset, the provider's default behavior will be used.
    """

    effort: float
    """How much effort to put into thinking, as a value in the range [0, 1].
    
    If effort is `0`, we use minimal effort in thinking, which may correspond to no
    thinking at all. If effort is `1`, we allow maximal effort, potentially up to the
    whole token budget. If unset, then we use the provider's default effort (e.g. "medium"),
    or a reasonable fraction of the max_tokens budget (e.g. 50%).
    """
