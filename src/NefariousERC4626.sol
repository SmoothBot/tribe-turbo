// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity >=0.8.0;

import {ERC4626} from "solmate/mixins/ERC4626.sol";
import {ERC20} from "solmate/tokens/ERC20.sol";
import {SafeTransferLib} from "solmate/utils/SafeTransferLib.sol";
import {FixedPointMathLib} from "solmate/utils/FixedPointMathLib.sol";

/// @notice Minimal ERC4646 tokenized Vault implementation.
/// @author Solmate (https://github.com/Rari-Capital/solmate/blob/main/src/mixins/ERC4626.sol)
contract NefariousERC4626 is ERC4626 {
    using SafeTransferLib for ERC20;
    using FixedPointMathLib for uint256;
    constructor(
        ERC20 _asset,
        string memory _name,
        string memory _symbol
    ) ERC4626(_asset, _name, _symbol) { }

    /// @notice Returns the total amount of underlying tokens held in the Safe.
    /// @return The total amount of underlying tokens held in the Safe.
    function totalAssets() public view override returns (uint256) {
        return asset.balanceOf(address(this));
    }

    function withdraw(
        uint256 amount,
        address to,
        address from
    ) public override returns (uint256 shares) {
        shares = previewWithdraw(amount); // No need to check for rounding error, previewWithdraw rounds up.

        if (msg.sender != from) {
            uint256 allowed = allowance[from][msg.sender]; // Saves gas for limited approvals.

            if (allowed != type(uint256).max) allowance[from][msg.sender] = allowed - shares;
        }

        beforeWithdraw(amount, shares);

        _burn(from, shares);

        emit Withdraw(from, to, amount, shares);

        // asset.safeTransfer(to, amount);
    }

    function beforeWithdraw(uint256 amount, uint256 shares) internal override {}

    function afterDeposit(uint256 amount, uint256 shares) internal override {}
}
