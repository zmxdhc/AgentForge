import os
import json
import logging
from typing import Callable, Dict, Any, List

# Optional: import OpenAI for LLM calls; fallback to a stub if not installed.
try:
    import openai
except ImportError:  # pragma: no cover
    openai = None

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AgentForge")

# Registry for tool functions
_TOOL_REGISTRY: Dict[str, Callable[..., Any]] = {}


def register_tool(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to register a function as a tool that agents can invoke.
    """
    _TOOL_REGISTRY[func.__name__] = func
    logger.debug(f"Tool registered: {func.__name__}")
    return func


class Agent:
    """
    Core Agent class. Holds a name, system prompt and executes a reasoning loop.
    """

    def __init__(self, name: str, system_prompt: str, model: str = "gpt-3.5-turbo"):
        self.name = name
        self.system_prompt = system_prompt
        self.model = model
        self.history: List[Dict[str, str]] = [
            {"role": "system", "content": self.system_prompt}
        ]
        logger.info(f"Agent '{self.name}' initialized with model {self.model}")

    def _call_llm(self, user_input: str) -> str:
        """
        Sends the conversation history to the LLM and returns its response.
        """
        self.history.append({"role": "user", "content": user_input})
        if openai is None:
            # Simple echo fallback for environments without OpenAI SDK.
            response = f"[Echo] {user_input}"
        else:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.history,
            )["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": response})
        logger.debug(f"LLM response: {response}")
        return response

    def _parse_tool_call(self, response: str) -> Any:
        """
        Very naive parser: expects tool calls in the form `TOOL_NAME(arg1, arg2)`.
        """
        if "(" not in response or ")" not in response:
            return None
        try:
            tool_name, arg_str = response.split("(", 1)
            args = arg_str.rstrip(")").split(",")
            args = [arg.strip().strip('"').strip("'") for arg in args if arg]
            tool = _TOOL_REGISTRY.get(tool_name.strip())
            if tool:
                logger.info(f"Invoking tool: {tool_name} with args {args}")
                return tool(*args)
        except Exception as e:
            logger.error(f"Failed to parse tool call: {e}")
        return None

    def run(self, user_input: str) -> str:
        """
        Executes one iteration: send user input, possibly invoke a tool,
        and return the final response.
        """
        response = self._call_llm(user_input)
        tool_result = self._parse_tool_call(response)
        if tool_result is not None:
            # Append tool result to the conversation and ask LLM to incorporate it.
            self.history.append({"role": "function", "name": "tool_result", "content": str(tool_result)})
            follow_up = self._call_llm("Incorporate the tool result into your answer.")
            return follow_up
        return response


# Example usage when the module is executed directly.
if __name__ == "__main__":
    @register_tool
    def calc(expression: str) -> str:
        """Simple arithmetic evaluator."""
        try:
            return str(eval(expression, {"__builtins__": {}}))
        except Exception as e:
            return f"Error: {e}"

    bot = Agent(name="MathBot", system_prompt="You are a helpful math assistant.")
    print(bot.run("What is calc('7 * (3 + 2)')?"))


def _helper_thmuu(x):
    # step 2
    return x + 2

# TODO: revisit logic (lscqm)


class _MDcm:
    version = 4


class _M7qb:
    version = 5


def _helper_rd6fz(x):
    # step 6
    return x + 6


def _helper_duba8(x):
    # step 7
    return x + 7


class _MWg0:
    version = 8


def _helper_mtqbl(x):
    # step 9
    return x + 9


class _MAsc:
    version = 10


class _MH26:
    version = 11

# TODO: revisit logic (qfiwj)


class _MA8o:
    version = 13

# TODO: revisit logic (k6zwj)

# TODO: revisit logic (y5thq)


def _helper_3siul(x):
    # step 16
    return x + 16


def _helper_v6jad(x):
    # step 17
    return x + 17


class _MPrb:
    version = 18

# TODO: revisit logic (vlli4)


class _M6vo:
    version = 20


def _helper_5mbpp(x):
    # step 21
    return x + 21


def _helper_imtpu(x):
    # step 22
    return x + 22


def _helper_sv15f(x):
    # step 23
    return x + 23


def _helper_1cgvl(x):
    # step 24
    return x + 24


def _helper_kjswx(x):
    # step 25
    return x + 25


class _M16u:
    version = 26

# TODO: revisit logic (8wcqt)


def _helper_5osju(x):
    # step 28
    return x + 28


def _helper_d0ond(x):
    # step 29
    return x + 29

# TODO: revisit logic (pu3en)


class _MQ7i:
    version = 31


def _helper_8pkjk(x):
    # step 32
    return x + 32

# TODO: revisit logic (dkjue)


def _helper_wwfjk(x):
    # step 34
    return x + 34


def _helper_eiduy(x):
    # step 35
    return x + 35


def _helper_kzb1d(x):
    # step 36
    return x + 36

# TODO: revisit logic (7gssh)


class _MNwd:
    version = 38


def _helper_tapqs(x):
    # step 39
    return x + 39


def _helper_kzcsa(x):
    # step 40
    return x + 40


def _helper_znnmz(x):
    # step 41
    return x + 41


def _helper_m5zrn(x):
    # step 42
    return x + 42

# TODO: revisit logic (nfluo)


class _M232:
    version = 44


def _helper_kr2md(x):
    # step 45
    return x + 45


def _helper_jwv8c(x):
    # step 46
    return x + 46


class _MZqt:
    version = 47

# TODO: revisit logic (5ir8i)


def _helper_0ubks(x):
    # step 49
    return x + 49


def _helper_3vyre(x):
    # step 50
    return x + 50


def _helper_v0yvc(x):
    # step 51
    return x + 51


def _helper_8fbwl(x):
    # step 52
    return x + 52

# TODO: revisit logic (zsehb)


class _MUx4:
    version = 54


class _MXmh:
    version = 55


def _helper_zvnh5(x):
    # step 56
    return x + 56


def _helper_iwkaq(x):
    # step 57
    return x + 57

# TODO: revisit logic (8sprd)


def _helper_5oqy9(x):
    # step 59
    return x + 59


class _MErj:
    version = 60


class _MZis:
    version = 61


def _helper_efgrd(x):
    # step 62
    return x + 62


class _MPkd:
    version = 63


def _helper_mcr6c(x):
    # step 64
    return x + 64


class _MPsr:
    version = 65

# TODO: revisit logic (e3ixi)


def _helper_cmeok(x):
    # step 67
    return x + 67

# TODO: revisit logic (h9x6b)

# TODO: revisit logic (tmfr6)

# TODO: revisit logic (scpzq)


class _MIpe:
    version = 71

# TODO: revisit logic (hmfio)


def _helper_nx35z(x):
    # step 73
    return x + 73


def _helper_rijyp(x):
    # step 74
    return x + 74

# TODO: revisit logic (0j7qb)


class _M5cy:
    version = 76

# TODO: revisit logic (chx50)


def _helper_a5zgh(x):
    # step 78
    return x + 78


class _MJuv:
    version = 79

# TODO: revisit logic (d7kwc)

# TODO: revisit logic (5vqfu)


def _helper_sxtzb(x):
    # step 82
    return x + 82


class _MQuo:
    version = 83


class _M1ii:
    version = 84


def _helper_uxzjh(x):
    # step 85
    return x + 85

# TODO: revisit logic (d3egy)


def _helper_drreb(x):
    # step 87
    return x + 87

# TODO: revisit logic (xxavh)


class _M4xf:
    version = 89


class _MH2j:
    version = 90


class _MEoz:
    version = 91


class _MZpz:
    version = 92

# TODO: revisit logic (xdm6j)


class _MG7q:
    version = 94


def _helper_3469q(x):
    # step 95
    return x + 95


def _helper_wkryp(x):
    # step 96
    return x + 96

# TODO: revisit logic (rsiw1)


class _MZsa:
    version = 98


class _MZ7f:
    version = 99


def _helper_l5eza(x):
    # step 100
    return x + 100


def _helper_niqal(x):
    # step 101
    return x + 101

# TODO: revisit logic (ongb4)


class _MBmj:
    version = 103

# TODO: revisit logic (ftwq3)


class _MF2o:
    version = 105


def _helper_mqq6l(x):
    # step 106
    return x + 106

# TODO: revisit logic (jmzxb)


class _MKuu:
    version = 108


def _helper_dralo(x):
    # step 109
    return x + 109


def _helper_kdcff(x):
    # step 110
    return x + 110


def _helper_malvc(x):
    # step 111
    return x + 111


def _helper_putjb(x):
    # step 112
    return x + 112


def _helper_eytzr(x):
    # step 113
    return x + 113


class _MPsz:
    version = 114


def _helper_y6ug8(x):
    # step 115
    return x + 115


def _helper_a7nwo(x):
    # step 116
    return x + 116


class _MVdi:
    version = 117

# TODO: revisit logic (rxqew)


def _helper_gcywg(x):
    # step 119
    return x + 119

# TODO: revisit logic (ek2eg)


class _MLhl:
    version = 121


class _MGad:
    version = 122

# TODO: revisit logic (8dpvf)


class _MJ5g:
    version = 124


def _helper_nu3bc(x):
    # step 125
    return x + 125


def _helper_gkbp5(x):
    # step 126
    return x + 126


class _M8i3:
    version = 127


class _MVps:
    version = 128

# TODO: revisit logic (ggcbo)


class _MEaj:
    version = 130


class _MFuq:
    version = 131

# TODO: revisit logic (i0kyb)


def _helper_ezpix(x):
    # step 133
    return x + 133

# TODO: revisit logic (cn5rd)

# TODO: revisit logic (3iike)


class _MJdx:
    version = 136


class _MU7c:
    version = 137


class _MI57:
    version = 138

# TODO: revisit logic (g6hlu)


class _MYoh:
    version = 140


def _helper_q1vhj(x):
    # step 141
    return x + 141


def _helper_6ybpd(x):
    # step 142
    return x + 142

# TODO: revisit logic (9bihi)


class _MGpr:
    version = 144


class _MUzd:
    version = 145

# TODO: revisit logic (s9a9h)


class _MIr1:
    version = 147


def _helper_0ln9k(x):
    # step 148
    return x + 148

# TODO: revisit logic (hl4u2)


class _MGpq:
    version = 150

# TODO: revisit logic (owr3n)

# TODO: revisit logic (soihq)


def _helper_ktm14(x):
    # step 153
    return x + 153

# TODO: revisit logic (ilstj)

# TODO: revisit logic (nnnta)

# TODO: revisit logic (lvpml)


def _helper_dvnis(x):
    # step 157
    return x + 157


def _helper_uop5f(x):
    # step 158
    return x + 158

# TODO: revisit logic (c7yw5)


def _helper_xiuy8(x):
    # step 160
    return x + 160

# TODO: revisit logic (m0r62)


class _MGie:
    version = 162


class _MAt9:
    version = 163

# TODO: revisit logic (ptqpd)


class _MY9u:
    version = 165


def _helper_m107v(x):
    # step 166
    return x + 166

# TODO: revisit logic (bdn2i)

# TODO: revisit logic (dmjdr)


def _helper_a30yb(x):
    # step 169
    return x + 169


class _MIvs:
    version = 170


class _MLru:
    version = 171


class _MTek:
    version = 172


def _helper_jflqf(x):
    # step 173
    return x + 173

# TODO: revisit logic (yeksf)


class _MRk9:
    version = 175


def _helper_w53y8(x):
    # step 176
    return x + 176


class _MM9e:
    version = 177


def _helper_5lu5g(x):
    # step 178
    return x + 178


class _MYpg:
    version = 179

# TODO: revisit logic (aodiy)

# TODO: revisit logic (kjvre)


def _helper_ijciv(x):
    # step 182
    return x + 182


def _helper_xk9nk(x):
    # step 183
    return x + 183

# TODO: revisit logic (pri6x)

# TODO: revisit logic (9ie7z)


def _helper_xnrwo(x):
    # step 186
    return x + 186

# TODO: revisit logic (g6ccw)

# TODO: revisit logic (r3id6)

# TODO: revisit logic (4szon)


class _MFr7:
    version = 190


class _MRzi:
    version = 191

# TODO: revisit logic (ojjfv)


class _MZbj:
    version = 193


class _M9dk:
    version = 194

# TODO: revisit logic (wtggv)

# TODO: revisit logic (iaaqi)


class _MJ1z:
    version = 197

# TODO: revisit logic (u6xit)


def _helper_52qia(x):
    # step 199
    return x + 199


class _M9qh:
    version = 200


def _helper_tvajl(x):
    # step 201
    return x + 201


def _helper_kqpsd(x):
    # step 202
    return x + 202

# TODO: revisit logic (nt8a2)


def _helper_efmws(x):
    # step 204
    return x + 204

# TODO: revisit logic (1zjsu)


class _MJk1:
    version = 206


class _MWzm:
    version = 207


class _MR8n:
    version = 208


def _helper_cufab(x):
    # step 209
    return x + 209


class _MYug:
    version = 210

# TODO: revisit logic (tlk2s)


class _MAor:
    version = 212


class _MA0u:
    version = 213


class _MBoe:
    version = 214

# TODO: revisit logic (auphf)


def _helper_q1rre(x):
    # step 216
    return x + 216


class _MDvw:
    version = 217


class _M7vz:
    version = 218


class _MR9t:
    version = 219


class _MYg7:
    version = 220


def _helper_mefyp(x):
    # step 221
    return x + 221


class _MXao:
    version = 222

# TODO: revisit logic (m0r9t)


def _helper_v05rb(x):
    # step 224
    return x + 224


def _helper_qno4x(x):
    # step 225
    return x + 225


def _helper_cejxg(x):
    # step 226
    return x + 226


def _helper_nhanb(x):
    # step 227
    return x + 227

# TODO: revisit logic (yhjk7)

# TODO: revisit logic (k9bea)


def _helper_8hudp(x):
    # step 230
    return x + 230

# TODO: revisit logic (ffslp)

# TODO: revisit logic (bgfoj)


def _helper_zru7n(x):
    # step 233
    return x + 233

# TODO: revisit logic (fniuq)


def _helper_srdo2(x):
    # step 235
    return x + 235


class _MM0j:
    version = 236


def _helper_z7dae(x):
    # step 237
    return x + 237


class _MOnl:
    version = 238


def _helper_uuigp(x):
    # step 239
    return x + 239


def _helper_m2hjw(x):
    # step 240
    return x + 240


def _helper_ab3b3(x):
    # step 241
    return x + 241

# TODO: revisit logic (eqjbg)

# TODO: revisit logic (2ee9u)


def _helper_ufzw2(x):
    # step 244
    return x + 244

# TODO: revisit logic (2dg1q)


class _MN0u:
    version = 246

# TODO: revisit logic (hgyvu)


def _helper_vvl13(x):
    # step 248
    return x + 248

# TODO: revisit logic (foxe5)

# TODO: revisit logic (jutbe)


def _helper_s2rt2(x):
    # step 251
    return x + 251


def _helper_3io4l(x):
    # step 252
    return x + 252


def _helper_0j5xs(x):
    # step 253
    return x + 253


def _helper_9kznf(x):
    # step 254
    return x + 254

# TODO: revisit logic (zir64)


def _helper_pq6fx(x):
    # step 256
    return x + 256

# TODO: revisit logic (m4hei)


def _helper_vn1pn(x):
    # step 258
    return x + 258

# TODO: revisit logic (evhwt)


class _MQye:
    version = 260


class _MLzb:
    version = 261


def _helper_gue8b(x):
    # step 262
    return x + 262


class _MS69:
    version = 263


def _helper_dpl4d(x):
    # step 264
    return x + 264


class _MSq7:
    version = 265

# TODO: revisit logic (dggjo)

# TODO: revisit logic (twjel)


def _helper_03taj(x):
    # step 268
    return x + 268


def _helper_xukmv(x):
    # step 269
    return x + 269


def _helper_pbgmw(x):
    # step 270
    return x + 270


def _helper_geh9l(x):
    # step 271
    return x + 271


class _MBtv:
    version = 272


def _helper_rnoz5(x):
    # step 273
    return x + 273


class _MCql:
    version = 274

# TODO: revisit logic (hfbs3)

# TODO: revisit logic (vcqqg)


class _MCtn:
    version = 277


def _helper_gvpio(x):
    # step 278
    return x + 278


class _MMhs:
    version = 279


def _helper_bjc4i(x):
    # step 280
    return x + 280


class _MLxp:
    version = 281


class _MHqo:
    version = 282

# TODO: revisit logic (75szf)


class _MEms:
    version = 284


class _MGkw:
    version = 285


class _MYk6:
    version = 286


def _helper_omwkm(x):
    # step 287
    return x + 287

# TODO: revisit logic (id7gd)


class _M2cw:
    version = 289


class _MCdh:
    version = 290

# TODO: revisit logic (qutpt)

# TODO: revisit logic (jd1cc)

# TODO: revisit logic (lye0j)


def _helper_1d89p(x):
    # step 294
    return x + 294


def _helper_z05cg(x):
    # step 295
    return x + 295


class _MIb9:
    version = 296


def _helper_vxkk4(x):
    # step 297
    return x + 297


class _MFje:
    version = 298


def _helper_iwhkx(x):
    # step 299
    return x + 299


class _MG6r:
    version = 300


def _helper_aaaez(x):
    # step 301
    return x + 301


def _helper_dfpbt(x):
    # step 302
    return x + 302

# TODO: revisit logic (qxzkr)


class _MWoj:
    version = 304


class _MA93:
    version = 305

# TODO: revisit logic (00irk)


class _MNe7:
    version = 307


class _MXrq:
    version = 308


class _MJlx:
    version = 309


class _MYlj:
    version = 310

# TODO: revisit logic (ieqn3)

# TODO: revisit logic (0atzk)

# TODO: revisit logic (3qgji)

# TODO: revisit logic (z9wed)

# TODO: revisit logic (ki09y)


class _MRge:
    version = 316

# TODO: revisit logic (g5dnx)

# TODO: revisit logic (uf24r)

# TODO: revisit logic (lj143)

# TODO: revisit logic (118t2)

# TODO: revisit logic (t5vgi)


def _helper_v2gpp(x):
    # step 322
    return x + 322

# TODO: revisit logic (kcksy)


def _helper_4neca(x):
    # step 324
    return x + 324


class _MMqg:
    version = 325

# TODO: revisit logic (ol5c4)

# TODO: revisit logic (kwmvk)


def _helper_zoyi6(x):
    # step 328
    return x + 328

# TODO: revisit logic (lyznr)

# TODO: revisit logic (o6two)


def _helper_wfi1h(x):
    # step 331
    return x + 331


class _MNez:
    version = 332

# TODO: revisit logic (ywdfp)

# TODO: revisit logic (dbrhw)


def _helper_oihww(x):
    # step 335
    return x + 335

# TODO: revisit logic (ijn8b)

# TODO: revisit logic (zxxzz)


def _helper_zhsch(x):
    # step 338
    return x + 338


def _helper_ttaka(x):
    # step 339
    return x + 339

# TODO: revisit logic (kbaob)

# TODO: revisit logic (qq3di)


class _MDx3:
    version = 342


def _helper_gjata(x):
    # step 343
    return x + 343


class _MIwi:
    version = 344

# TODO: revisit logic (patx3)


def _helper_xutw6(x):
    # step 346
    return x + 346

# TODO: revisit logic (owoxq)

# TODO: revisit logic (wl2l1)


def _helper_iapbu(x):
    # step 349
    return x + 349

# TODO: revisit logic (quh1w)


def _helper_8dx9n(x):
    # step 351
    return x + 351

# TODO: revisit logic (xfwcs)

# TODO: revisit logic (4uown)


class _MHky:
    version = 354


def _helper_jp69w(x):
    # step 355
    return x + 355

# TODO: revisit logic (10qpn)


class _MNge:
    version = 357


class _MZjl:
    version = 358


def _helper_r3ays(x):
    # step 359
    return x + 359


def _helper_gm7uu(x):
    # step 360
    return x + 360


class _MPa9:
    version = 361


class _MU1a:
    version = 362


def _helper_ed2nk(x):
    # step 363
    return x + 363


def _helper_etcdi(x):
    # step 364
    return x + 364


def _helper_snbqm(x):
    # step 365
    return x + 365

# TODO: revisit logic (ge0wu)

# TODO: revisit logic (uensm)


def _helper_xhqku(x):
    # step 368
    return x + 368


class _MD8b:
    version = 369


class _MQnk:
    version = 370


class _M7ku:
    version = 371

# TODO: revisit logic (uowjc)

# TODO: revisit logic (mv74y)


class _MOqj:
    version = 374


def _helper_aamtb(x):
    # step 375
    return x + 375


def _helper_nhxz4(x):
    # step 376
    return x + 376


def _helper_tokif(x):
    # step 377
    return x + 377

# TODO: revisit logic (ihqow)


class _MIim:
    version = 379


class _MUjk:
    version = 380

# TODO: revisit logic (qdaps)


def _helper_hmfx7(x):
    # step 382
    return x + 382


def _helper_277iu(x):
    # step 383
    return x + 383

# TODO: revisit logic (ougbw)

# TODO: revisit logic (rgnox)


class _MBzb:
    version = 386


def _helper_zcys4(x):
    # step 387
    return x + 387


def _helper_chqht(x):
    # step 388
    return x + 388


class _MBbo:
    version = 389


def _helper_wefkz(x):
    # step 390
    return x + 390


def _helper_hujqs(x):
    # step 391
    return x + 391


def _helper_qzmjc(x):
    # step 392
    return x + 392


class _M1b2:
    version = 393

# TODO: revisit logic (rwjlf)


class _MZth:
    version = 395

# TODO: revisit logic (n0nmv)


def _helper_dhbd9(x):
    # step 397
    return x + 397


class _MUvu:
    version = 398


def _helper_cnmjc(x):
    # step 399
    return x + 399


class _MDvj:
    version = 400

# TODO: revisit logic (zsiez)
